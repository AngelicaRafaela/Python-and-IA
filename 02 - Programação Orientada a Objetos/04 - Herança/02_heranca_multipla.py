class Animal:
    def __init__(self, nro_patas):
        # Método especial __init__ que inicializa o número de patas do animal
        self.nro_patas = nro_patas

    def __str__(self):
        # Método especial __str__ que retorna uma representação em string do objeto
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        # Método especial __init__ que inicializa a cor do pelo do mamífero
        self.cor_pelo = cor_pelo
        # Chama o __init__ da classe pai (Animal) para inicializar o número de patas
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        # Método especial __init__ que inicializa a cor do bico da ave
        self.cor_bico = cor_bico
        # Chama o __init__ da classe pai (Animal) para inicializar o número de patas
        super().__init__(**kw)


class Gato(Mamifero):
    pass
    # Não adiciona novos atributos ou métodos, apenas herda da classe Mamifero

class FalarMixin:
    def falar(self):
        return "Oi, estou falando!"
class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        # Método especial __init__ que inicializa a cor do bico, cor do pelo e número de patas do ornitorrinco
        # Chama o __init__ das classes pai (Mamifero e Ave) para inicializar os atributos correspondentes
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)


# Instanciação de objetos e exemplos de uso:

# Cria um objeto da classe Gato com o número de patas e a cor do pelo especificados
gato = Gato(nro_patas=4, cor_pelo="Preto")
# Imprime a representação em string do objeto gato
print(gato)

# Cria um objeto da classe Ornitorrinco com o número de patas, cor do pelo e cor do bico especificados
ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
# Imprime a representação em string do objeto ornitorrinco
print(ornitorrinco)
print(ornitorrinco.falar())
