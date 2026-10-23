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
        if nome == "" or nota < 0 or nota > 99.99:
            return False
        self.alunos.append(Aluno(nome, nota))
        return True

    def calcular_media(self):
        if len(self.alunos) == 0:
            return 0
        total = 0
        for aluno in self.alunos:
            total += aluno.nota
        return total / len(self.alunos)

def alunoCobol():
    turma = Turma()
    print("=== SISTEMA DE CADASTRO DE ALUNOS ===")

    for numero in range(1, 6):
        while True:
            nome = input(f"Digite o nome do aluno {numero}: ").strip()
            try:
                nota = float(input(f"Digite a nota de {nome}: ").replace(",", "."))
                if turma.cadastrar_aluno(nome, nota):
                    break
                print("Informe um nome e nota entre 0 e 99,99.")
            except ValueError:
                print("Digite uma nota válida.")

    print("\n=== LISTA DE ALUNOS ===")
    for aluno in turma.alunos:
        print(f"{aluno.nome} | Nota: {aluno.nota:.2f}")
    print(f"Média da turma: {turma.calcular_media():.2f}")


alunoCobol()
