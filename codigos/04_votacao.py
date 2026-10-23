# Programa 4: Sistema de votacao (migrado de Java)

class SistemaVotacao:
    def __init__(self):
        self.opcoes = ["Opção 1", "Opção 2", "Opção 3"]
        self.votos = [0, 0, 0]

    def registrar_voto(self, escolha):
        if escolha >= 1 and escolha <= 3:
            self.votos[escolha - 1] += 1
            return True
        return False

    def obter_resultados(self):
        resultados = []
        for i in range(3):
            resultados.append((self.opcoes[i], self.votos[i]))
        return resultados


def votacao():
    sistema = SistemaVotacao()
    print("=== SISTEMA DE VOTAÇÃO ===")
    print("1 - Opção 1")
    print("2 - Opção 2")
    print("3 - Opção 3")

    while True:
        entrada = input("Escolha uma opção (1-3) ou 0 para encerrar: ")

        if not entrada.isdigit():
            print("Digite apenas números.")
            continue

        escolha = int(entrada)
        if escolha == 0:
            break
        elif sistema.registrar_voto(escolha):
            print(f"Você votou na Opção {escolha}")
        else:
            print("Opção inválida.")

    print("\n=== RESULTADOS FINAIS ===")
    for opcao, votos in sistema.obter_resultados():
        print(f"{opcao}: {votos} voto(s)")


votacao()
