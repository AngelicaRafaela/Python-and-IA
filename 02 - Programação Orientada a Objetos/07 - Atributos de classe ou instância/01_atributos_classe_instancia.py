class Estudante:
    # Atributo de classe para armazenar o nome da escola (compartilhado por todas as instâncias)
    escola = "DIO"

    def __init__(self, nome, matricula):
        # Método especial __init__ para inicializar os atributos nome e matrícula para cada estudante
        self.nome = nome  # Atributo de instância para armazenar o nome do estudante
        self.matricula = matricula  # Atributo de instância para armazenar a matrícula do estudante

    def __str__(self) -> str:
        # Método especial __str__ para retornar uma representação em string do objeto Estudante
        return f"{self.nome} - {self.matricula} - {self.escola}"  # Retorna uma string com o nome, matrícula e nome da escola


def mostrar_valores(*objs):
    # Função para exibir os valores de cada objeto Estudante
    for obj in objs:
        print(obj)  # Imprime cada objeto Estudante


# Cria instâncias de Estudante e chama a função mostrar_valores para exibi-las
aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)  # Exibe os valores dos primeiros dois alunos

# Altera o atributo de classe escola 'DIO' para 'Python'
Estudante.escola = "Python"

# Cria uma nova instância de Estudante e chama a função mostrar_valores para exibi-la junto com os outros alunos
aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)  # Exibe os valores dos três alunos, incluindo o novo valor da escola
