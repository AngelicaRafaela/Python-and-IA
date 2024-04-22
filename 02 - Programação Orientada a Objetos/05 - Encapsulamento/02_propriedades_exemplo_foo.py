class Foo:
    def __init__(self, x=None):
        # Método especial __init__ que inicializa o atributo _x
        self._x = x

    @property
    def x(self):
        # Método getter (propriedade) para acessar o valor de _x
        # Retorna o valor de _x se existir, caso contrário retorna 0
        return self._x or 0

    @x.setter
    def x(self, value):
        # Método setter para definir o valor de _x
        # Incrementa o valor de _x com o valor passado como parâmetro
        self._x += value

    @x.deleter
    def x(self):
        # Método deleter para redefinir o valor de _x para 0
        self._x = 0


# Instancia um objeto da classe Foo com o valor inicial de _x igual a 10
foo = Foo(10)
# Imprime o valor de _x usando a propriedade x (getter)
print(foo.x)
# Deleta o valor de _x usando o deleter da propriedade x
del foo.x
# Imprime o valor de _x após deletar usando a propriedade x (getter)
print(foo.x)
# Define o valor de _x usando a propriedade x (setter)
foo.x = 10
# Imprime o valor de _x após definir usando a propriedade x (getter)
print(foo.x)
