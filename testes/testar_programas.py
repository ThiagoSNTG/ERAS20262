"""Testes simples dos quatro programas migrados.
Execute: python testes/testar_programas.py (a partir da pasta de entrega).
"""
import importlib.util
from pathlib import Path
import sqlite3
import subprocess
import sys
import unittest

PASTA = Path(__file__).resolve().parents[1]


def carregar(arquivo, nome_modulo):
    caminho = PASTA / 'codigos' / arquivo
    spec = importlib.util.spec_from_file_location(nome_modulo, caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


funcionarios = carregar('01_funcionarios.py', 'funcionarios')
alunos_java = carregar('02_alunos_java.py', 'alunos_java')
alunos_cobol = carregar('03_alunos_cobol.py', 'alunos_cobol')
votacao = carregar('04_votacao.py', 'votacao')


class TestesMigracao(unittest.TestCase):
    def test_funcionarios_cadastro_e_busca(self):
        sistema = funcionarios.SistemaFuncionarios()
        self.assertTrue(sistema.adicionar_funcionario('Ana', 'Analista', 3200.0))
        self.assertEqual(sistema.buscar_funcionario('Ana').cargo, 'Analista')
        self.assertEqual(len(sistema.listar_funcionarios()), 1)
        self.assertIsNone(sistema.buscar_funcionario('Inexistente'))

    def test_funcionarios_limite(self):
        sistema = funcionarios.SistemaFuncionarios()
        for numero in range(100):
            self.assertTrue(sistema.adicionar_funcionario(f'Nome {numero}', 'Auxiliar', 1000))
        self.assertFalse(sistema.adicionar_funcionario('Nome 101', 'Auxiliar', 1000))
        self.assertFalse(sistema.adicionar_funcionario('', 'Auxiliar', 1000))

    def test_alunos_java_consulta(self):
        sistema = alunos_java.SistemaAlunos()
        sistema.adicionar_aluno('Beatriz', 8.5)
        self.assertEqual(sistema.buscar_nota('Beatriz'), 8.5)
        self.assertIsNone(sistema.buscar_nota('Inexistente'))

    def test_alunos_java_nome_repetido_compatibilidade(self):
        sistema = alunos_java.SistemaAlunos()
        sistema.adicionar_aluno('João', 6.0)
        sistema.adicionar_aluno('João', 8.0)
        self.assertEqual(sistema.listar_alunos(), [('João', 8.0), ('João', 8.0)])

    def test_cobol_media_cinco(self):
        turma = alunos_cobol.Turma()
        for nome, nota in [('A', 8), ('B', 6), ('C', 7), ('D', 9), ('E', 10)]:
            self.assertTrue(turma.cadastrar_aluno(nome, nota))
        self.assertEqual(turma.calcular_media(), 8)
        self.assertFalse(turma.cadastrar_aluno('Sexto', 5))

    def test_cobol_notas_aceitas(self):
        turma = alunos_cobol.Turma()
        self.assertFalse(turma.cadastrar_aluno('A', 100))
        self.assertFalse(turma.cadastrar_aluno('A', -1))
        self.assertTrue(turma.cadastrar_aluno('A', 99.99))

    def test_votacao_totais(self):
        sistema = votacao.SistemaVotacao()
        self.assertTrue(sistema.registrar_voto(1))
        self.assertTrue(sistema.registrar_voto(3))
        self.assertTrue(sistema.registrar_voto(3))
        self.assertFalse(sistema.registrar_voto(4))
        self.assertEqual(sistema.votos, [1, 0, 2])

    def test_sql_proposto_execucao(self):
        for caminho in sorted((PASTA / 'banco_de_dados').glob('*.sql')):
            with self.subTest(arquivo=caminho.name):
                with sqlite3.connect(':memory:') as banco:
                    banco.executescript(caminho.read_text(encoding='utf-8'))
                    tabelas = banco.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
                    self.assertTrue(tabelas)

    def test_execucao_terminal_funcionarios(self):
        resposta = self.rodar_cli('01_funcionarios.py', '1\nAna\nSecretária\n2000\n2\n3\nAna\n0\n')
        self.assertIn('Ana - Secretária', resposta)
        self.assertIn('Cargo: Secretária', resposta)

    def test_execucao_terminal_alunos_java(self):
        resposta = self.rodar_cli('02_alunos_java.py', '1\nAna\n7.5\n3\nAna\n0\n')
        self.assertIn('Nota de Ana: 7.5', resposta)

    def test_execucao_terminal_alunos_cobol(self):
        resposta = self.rodar_cli('03_alunos_cobol.py', 'A\n8\nB\n6\nC\n7\nD\n9\nE\n10\n')
        self.assertIn('Média da turma: 8.00', resposta)

    def test_execucao_terminal_votacao(self):
        resposta = self.rodar_cli('04_votacao.py', '1\n3\n3\n0\n')
        self.assertIn('Opção 1: 1 voto(s)', resposta)
        self.assertIn('Opção 3: 2 voto(s)', resposta)

    @staticmethod
    def rodar_cli(arquivo, dados):
        processo = subprocess.run(
            [sys.executable, str(PASTA / 'codigos' / arquivo)],
            input=dados, capture_output=True, text=True, timeout=8,
            encoding='utf-8'
        )
        if processo.returncode:
            raise AssertionError(processo.stderr)
        return processo.stdout


if __name__ == '__main__':
    unittest.main(verbosity=2)
