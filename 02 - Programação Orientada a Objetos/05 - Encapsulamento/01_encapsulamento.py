class Conta:
    def __init__(self, nro_agencia, saldo=0):
        # Método especial __init__ que inicializa os atributos da conta
        self._saldo = saldo  # Atributo protegido para armazenar o saldo da conta
        self.nro_agencia = nro_agencia  # Atributo público para armazenar o número da agência

    def depositar(self, valor):
        # Método para realizar um depósito na conta
        # Incrementa o valor do depósito ao saldo da conta
        self._saldo += valor

    def sacar(self, valor):
        # Método para realizar um saque na conta
        # Decrementa o valor do saque do saldo da conta
        self._saldo -= valor

    def mostrar_saldo(self):
        # Método para exibir o saldo atual da conta
        # Retorna o valor do saldo
        return self._saldo


# Instancia um objeto da classe Conta com o número da agência "0001" e saldo inicial de 100
conta = Conta("0001", 100)
# Realiza um depósito de 100 na conta
conta.depositar(100)
# Imprime o número da agência da conta
print(conta.nro_agencia)
# Imprime o saldo atual da conta
print(conta.mostrar_saldo())

