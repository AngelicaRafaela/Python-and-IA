class MeuIterador:
    def __init__(self, numeros: list[int]):
        # Inicializa o iterador com a lista de números e define um contador para rastrear a posição atual na lista
        self.numeros = numeros
        self.contador = 0
    
    def __iter__(self):
        # Retorna o próprio objeto como iterador
        return self
    
    def __next__(self):
        try:
            # Tenta obter o próximo número na lista e multiplicá-lo por 2
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError:
            # Se não houver mais números na lista, levanta StopIteration para indicar o fim da iteração
            raise StopIteration

# Cria uma instância de MeuIterador com uma lista de números e itera sobre ela
for i in MeuIterador(numeros=[38, 13, 11]):
    # Para cada iteração, imprime o número da lista multiplicado por 2
    print(i)
