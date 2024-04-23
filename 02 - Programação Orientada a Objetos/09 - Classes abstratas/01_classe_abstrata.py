from abc import ABC, abstractmethod, abstractproperty

# Classe abstrata ControleRemoto que define métodos abstratos para ligar, desligar e obter a marca do dispositivo controlado
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @property
    @abstractproperty
    def marca(self):
        pass

# Classe Concreta ControleTV que herda da classe ControleRemoto e implementa os métodos ligar, desligar e a propriedade marca
class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"

# Classe Concreta ControleArCondicionado que herda da classe ControleRemoto e implementa os métodos ligar, desligar e a propriedade marca
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"

# Cria uma instância de ControleTV e executa os métodos ligar, desligar e imprime a marca
controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

# Cria uma instância de ControleArCondicionado e executa os métodos ligar, desligar e imprime a marca
controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
