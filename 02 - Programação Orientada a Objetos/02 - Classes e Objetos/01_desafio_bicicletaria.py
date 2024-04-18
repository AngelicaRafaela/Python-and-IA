class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        # Inicializa os atributos da bicicleta
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        # Método que emite o som da buzina da bicicleta
        print("Plim plim...")

    def parar(self):
        # Método que simula a ação de parar a bicicleta
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        # Método que simula a ação de correr com a bicicleta
        print("Vrummmmm...")

    def __str__(self):
        # Método especial que retorna uma representação em string da bicicleta
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


# Criação da primeira instância da bicicleta
b1 = Bicicleta("vermelha", "caloi", 2022, 600)
# Chama o método buzinar() da instância b1
b1.buzinar()
# Chama o método correr() da instância b1
b1.correr()
# Chama o método parar() da instância b1
b1.parar()
# Imprime os atributos da instância b1
print(b1.cor, b1.modelo, b1.ano, b1.valor)

# Criação da segunda instância da bicicleta
b2 = Bicicleta("verde", "monark", 2000, 189)
# Imprime a representação em string da instância b2
print(b2)
# Chama o método correr() da instância b2
b2.correr()
