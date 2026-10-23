class SistemaAlunos:
    def __init__(self):
        self.notas = {}
        self.lista_nomes = []

    def adicionar_aluno(self, nome, nota):
        if nome == "":
            return False
        self.notas[nome] = nota
        self.lista_nomes.append(nome)
        return True

    def listar_alunos(self):
        lista = []
        for nome in self.lista_nomes:
            lista.append((nome, self.notas[nome]))
        return lista

    def buscar_nota(self, nome):
        return self.notas.get(nome)


def alunosCadastro():
    sistema = SistemaAlunos()

    while True:
        print("\n=== SISTEMA DE ALUNOS ===")
        print("1 - Adicionar aluno")
        print("2 - Listar alunos")
        print("3 - Buscar nota")
        print("0 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            nome = input("Nome do aluno: ").strip()
            try:
                nota = float(input("Nota final: ").replace(",", "."))
                if sistema.adicionar_aluno(nome, nota):
                    print("Aluno cadastrado com sucesso!")
                else:
                    print("Nome inválido.")
            except ValueError:
                print("Digite uma nota válida.")

        elif opcao == "2":
            if len(sistema.lista_nomes) == 0:
                print("Nenhum aluno cadastrado.")
            for nome, nota in sistema.listar_alunos():
                print(f"- {nome} | Nota: {nota}")

        elif opcao == "3":
            nome = input("Nome do aluno: ")
            nota = sistema.buscar_nota(nome)
            if nota is None:
                print("Aluno não encontrado.")
            else:
                print(f"Nota de {nome}: {nota}")

        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

alunosCadastro()