"""Migração do arquivo main.cob (COBOL) para Python.
Solicita cinco alunos, calcula e exibe a média da turma.
"""


class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota


class Turma:
    def __init__(self):
        self.alunos = []
        self.quantidade = 5

    def cadastrar_aluno(self, nome, nota):
        if len(self.alunos) >= self.quantidade:
            return False
        if not nome.strip() or not 0 <= nota <= 99.99:
            return False
        self.alunos.append(Aluno(nome, nota))
        return True

    def calcular_media(self):
        if not self.alunos:
            return 0
        total_notas = sum(aluno.nota for aluno in self.alunos)
        return total_notas / len(self.alunos)


def main():
    turma = Turma()
    print("=== SISTEMA DE CADASTRO DE ALUNOS ===")

    for numero in range(1, turma.quantidade + 1):
        while True:
            nome = input(f"Digite o nome do aluno {numero}: ").strip()
            try:
                nota = float(input(f"Digite a nota de {nome}: ").replace(",", "."))
            except ValueError:
                print("Nota inválida. Tente novamente.")
                continue
            if turma.cadastrar_aluno(nome, nota):
                break
            print("Informe um nome e uma nota entre 0 e 99,99.")

    print("\n=== LISTA DE ALUNOS ===")
    for aluno in turma.alunos:
        print(f"{aluno.nome} | Nota: {aluno.nota:.2f}")
    print(f"Média da turma: {turma.calcular_media():.2f}")


if __name__ == "__main__":
    main()
