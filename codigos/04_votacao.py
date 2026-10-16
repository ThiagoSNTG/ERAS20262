"""Migração de SistemaDeVotacao.java (Java) para Python.
Contabiliza votos em três opções e mostra o total final.
"""


class SistemaVotacao:
    def __init__(self):
        self.opcoes = ["Opção 1", "Opção 2", "Opção 3"]
        self.votos = [0, 0, 0]

    def registrar_voto(self, escolha):
        if 1 <= escolha <= len(self.opcoes):
            self.votos[escolha - 1] += 1
            return True
        return False

    def obter_resultados(self):
        return list(zip(self.opcoes, self.votos))


def main():
    sistema = SistemaVotacao()
    print("=== SISTEMA DE VOTAÇÃO ===")
    print("As opções são:")
    for numero, descricao in enumerate(sistema.opcoes, start=1):
        print(f"{numero} - {descricao}")

    while True:
        entrada = input("\nEscolha uma opção (1-3) ou 0 para encerrar: ").strip()
        try:
            escolha = int(entrada)
        except ValueError:
            print("Entrada inválida. Digite apenas números.")
            continue

        if escolha == 0:
            break
        if sistema.registrar_voto(escolha):
            print(f"Você votou na {sistema.opcoes[escolha - 1]}")
        else:
            print("Opção inválida. Tente novamente.")

    print("\n=== RESULTADOS FINAIS ===")
    for descricao, quantidade in sistema.obter_resultados():
        print(f"{descricao}: {quantidade} voto(s)")


if __name__ == "__main__":
    main()
