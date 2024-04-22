class Pessoa:
    def __init__(self, nome, ano_nascimento):
        # Método especial __init__ que inicializa os atributos nome e _ano_nascimento
        self.nome = nome  # Atributo público para armazenar o nome da pessoa
        self._ano_nascimento = ano_nascimento  # Atributo protegido para armazenar o ano de nascimento da pessoa

    @property
    def idade(self):
        # Método getter (propriedade) para calcular a idade da pessoa
        # Define o ano atual
        _ano_atual = 2024
        # Calcula a idade subtraindo o ano de nascimento do ano atual
        return _ano_atual - self._ano_nascimento


# Instancia um objeto da classe Pessoa com o nome "Angélica" e ano de nascimento 1992
pessoa = Pessoa("Angélica", 1992)
# Imprime o nome e a idade da pessoa usando a propriedade idade (getter)
print(f"Nome: {pessoa.nome} \tIdade: {pessoa.idade}")
