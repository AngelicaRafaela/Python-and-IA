class Pessoa:
    def __init__(self, nome, idade):
        # Método de inicialização para atribuir nome e idade aos objetos Pessoa
        self.nome = nome  # Atributo de instância para armazenar o nome da pessoa
        self.idade = idade  # Atributo de instância para armazenar a idade da pessoa

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        # Método de classe para criar um objeto Pessoa a partir de uma data de nascimento e nome
        idade = 2022 - ano  # Calcula a idade com base no ano de nascimento
        return cls(nome, idade)  # Retorna uma nova instância de Pessoa com o nome e idade calculados

    @staticmethod
    def e_maior_idade(idade):
        # Método estático para verificar se uma pessoa é maior de idade com base na idade fornecida
        return idade >= 18  # Retorna True se a idade for maior ou igual a 18, caso contrário, retorna False


# Cria um objeto Pessoa usando o método de classe 'criar_de_data_nascimento'
p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)  # Imprime o nome e a idade da pessoa criada

# Chama o método estático 'e_maior_idade' para verificar se uma pessoa é maior de idade
print(Pessoa.e_maior_idade(18))  # Imprime True, pois 18 é considerado maior de idade
print(Pessoa.e_maior_idade(8))   # Imprime False, pois 8 não é considerado maior de idade
