"""Migração do arquivo main.c (C) para Python.
Cadastro, listagem e busca de até 100 funcionários.
"""


class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario


class SistemaFuncionarios:
    def __init__(self):
        self.funcionarios = []
        self.limite = 100

    def adicionar_funcionario(self, nome, cargo, salario):
        if len(self.funcionarios) >= self.limite:
            return False
        if not nome.strip() or not cargo.strip() or salario < 0:
            return False
        funcionario = Funcionario(nome, cargo, salario)
        self.funcionarios.append(funcionario)
        return True

    def listar_funcionarios(self):
        return self.funcionarios

    def buscar_funcionario(self, nome):
        for funcionario in self.funcionarios:
            if funcionario.nome == nome:
                return funcionario
        return None


def main():
    sistema = SistemaFuncionarios()

    while True:
        print("\n=== SISTEMA DE FUNCIONÁRIOS ===")
        print("1 - Adicionar funcionário")
        print("2 - Listar funcionários")
        print("3 - Buscar funcionário")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            if len(sistema.funcionarios) >= sistema.limite:
                print("Limite atingido!")
                continue
            nome = input("Nome: ").strip()
            cargo = input("Cargo: ").strip()
            try:
                salario = float(input("Salário: ").replace(",", "."))
            except ValueError:
                print("Salário inválido. Informe um número.")
                continue
            if sistema.adicionar_funcionario(nome, cargo, salario):
                print("Funcionário cadastrado!")
            else:
                print("Dados inválidos ou limite atingido.")

        elif opcao == "2":
            funcionarios = sistema.listar_funcionarios()
            if not funcionarios:
                print("Nenhum funcionário cadastrado.")
            else:
                print("\nLista de funcionários:")
                for numero, funcionario in enumerate(funcionarios, start=1):
                    print(f"{numero}) {funcionario.nome} - {funcionario.cargo} - R$ {funcionario.salario:.2f}")

        elif opcao == "3":
            nome = input("Nome do funcionário: ")
            funcionario = sistema.buscar_funcionario(nome)
            if funcionario:
                print(f"Cargo: {funcionario.cargo} | Salário: R$ {funcionario.salario:.2f}")
            else:
                print("Funcionário não encontrado.")

        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
