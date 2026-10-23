import os
import subprocess
import sys

pasta = os.path.dirname(os.path.abspath(__file__))

programas = {
    "1": ("Funcionários", "codigos/01_funcionarios.py"),
    "2": ("Alunos (Java)", "codigos/02_alunos_java.py"),
    "3": ("Média dos alunos (COBOL)", "codigos/03_alunos_cobol.py"),
    "4": ("Votação", "codigos/04_votacao.py"),
    "5": ("Executar testes", "testes/testar_programas.py")
}

while True:
    print("\n=== MIGRAÇÃO PARA PYTHON ===")
    for numero in programas:
        print(numero, "-", programas[numero][0])
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "0":
        break
    elif opcao in programas:
        arquivo = programas[opcao][1]
        caminho = os.path.join(pasta, arquivo)
        if os.path.isfile(caminho):
            subprocess.run([sys.executable, caminho])
        else:
            print("Arquivo não encontrado. Extraia o ZIP inteiro.")
    else:
        print("Opção inválida.")
