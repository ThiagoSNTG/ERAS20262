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
        if nome == "" or cargo == "" or salario < 0:
            return False
        self.funcionarios.append(Funcionario(nome, cargo, salario))
        return True

    def listar_funcionarios(self):
        return self.funcionarios

    def buscar_funcionario(self, nome):
        for funcionario in self.funcionarios:
            if funcionario.nome == nome:
                return funcionario
        return None

def cadastroFuncionários():
    sistema = SistemaFuncionarios()

    while True:
        print("\n=== SISTEMA DE FUNCIONÁRIOS ===")
        print("1 - Adicionar funcionário")
        print("2 - Listar funcionários")
        print("3 - Buscar funcionário")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ").strip()
            cargo = input("Cargo: ").strip()
            try:
                salario = float(input("Salário: ").replace(",", "."))
                if sistema.adicionar_funcionario(nome, cargo, salario):
                    print("Funcionário cadastrado!")
                else:
                    print("Dados inválidos ou limite de 100 atingido.")
            except ValueError:
                print("Digite um salário válido.")

        elif opcao == "2":
            if len(sistema.funcionarios) == 0:
                print("Nenhum funcionário cadastrado.")
            for funcionario in sistema.listar_funcionarios():
                print(f"{funcionario.nome} - {funcionario.cargo} - R$ {funcionario.salario:.2f}")

        elif opcao == "3":
            nome = input("Nome do funcionário: ")
            funcionario = sistema.buscar_funcionario(nome)
            if funcionario is None:
                print("Funcionário não encontrado.")
            else:
                print(f"Cargo: {funcionario.cargo} | Salário: R$ {funcionario.salario:.2f}")

        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")

cadastroFuncionários()
