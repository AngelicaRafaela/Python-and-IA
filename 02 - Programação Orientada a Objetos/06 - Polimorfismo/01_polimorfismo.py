class Passaro:
    def voar(self):
        # Método que define o comportamento de voar genérico para pássaros
        print("Voando...")


class Pardal(Passaro):
    def voar(self):
        # Método que substitui o comportamento de voar para o pardal
        print("Pardal pode voar")


class Avestruz(Passaro):
    def voar(self):
        # Método que substitui o comportamento de voar para a avestruz
        print("Avestruz não pode voar")


# Exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        # Método que substitui o comportamento de voar para o avião
        print("Avião está decolando...")


def plano_voo(obj):
    # Função que recebe um objeto e chama o método voar do objeto
    obj.voar()


# Cria instâncias de cada classe e chama a função plano_voo para cada uma delas
plano_voo(Pardal())  # O pardal pode voar
plano_voo(Avestruz())  # A avestruz não pode voar
plano_voo(Aviao())  # O avião está decolando
