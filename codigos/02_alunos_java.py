"""Migração de SistemaAlunos.java (Java) para Python.
Mantém a lista de nomes e o dicionário de notas do original.
"""


class SistemaAlunos:
    def __init__(self):
        self.notas = {}
        self.lista_nomes = []

    def adicionar_aluno(self, nome, nota):
        if not nome.strip():
            return False
        self.notas[nome] = nota
        self.lista_nomes.append(nome)
        return True

    def listar_alunos(self):
        return [(nome, self.notas[nome]) for nome in self.lista_nomes]

    def buscar_nota(self, nome):
        return self.notas.get(nome)


def main():
    sistema = SistemaAlunos()

    while True:
        print("\n=== SISTEMA DE ALUNOS ===")
        print("1 - Adicionar aluno")
        print("2 - Listar alunos")
        print("3 - Buscar nota")
        print("0 - Sair")
        opcao = input("Opção: ").strip()

        if opcao == "1":
            nome = input("Nome do aluno: ").strip()
            try:
                nota = float(input("Nota final: ").replace(",", "."))
            except ValueError:
                print("Nota inválida. Informe um número.")
                continue
            if sistema.adicionar_aluno(nome, nota):
                print("Aluno cadastrado com sucesso!")
            else:
                print("Informe um nome válido.")

        elif opcao == "2":
            alunos = sistema.listar_alunos()
            if not alunos:
                print("Nenhum aluno cadastrado.")
            else:
                print("\nLista de alunos:")
                for nome, nota in alunos:
                    print(f"- {nome} | Nota: {nota}")

        elif opcao == "3":
            nome = input("Nome do aluno: ")
            nota = sistema.buscar_nota(nome)
            if nota is not None:
                print(f"Nota de {nome}: {nota}")
            else:
                print("Aluno não encontrado.")

        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
