import textwrap
from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime, timedelta
from pathlib import Path
import csv
import os

ROOT_PATH = Path(__file__).parent

def log_transacao_arquivo(funcao):
    # Decorador para registrar as transações em um arquivo CSV
    def envelope(*args, **kwargs):
        # Obter o caminho completo do arquivo de log
        log_path = ROOT_PATH / "log.csv"
        
        # Verificar se o arquivo de log já existe
        log_exist = os.path.exists(log_path)
        
        # Abrir o arquivo CSV no modo de escrita, com 'newline' vazio para evitar linhas em branco
        with open(log_path, mode='a', newline='') as file:
            # Criar o escritor CSV
            writer = csv.writer(file)
            
            # Escrever o cabeçalho do CSV, se o arquivo acabou de ser criado
            if not log_exist:
                writer.writerow(['Data e Hora', 'Função', 'Argumentos', 'Valor Retornado'])

            # Obter a data e hora atuais
            data_hora = datetime.now().strftime('%d-%m-%Y %H:%M')

            # Escrever os dados da transação no arquivo CSV
            writer.writerow([data_hora, funcao.__name__, args, kwargs])

        # Chamar a função original e retornar o resultado
        return funcao(*args, **kwargs)
    return envelope


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    @log_transacao_arquivo
    def realizar_transacao(self, conta, transacao):
        # Método para realizar uma transação em uma conta associada ao cliente
        transacao.registrar(conta)

    @log_transacao_arquivo
    def adicionar_conta(self, conta):
        # Método para adicionar uma nova conta à lista de contas do cliente
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        # Inicialização de um cliente do tipo Pessoa Física
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}: ({self.cpf})>"

class Conta:
    MAX_TRANSACTIONS_PER_DAY = 2  # Limite de transações diárias

    def __init__(self, numero, cliente):
        # Inicialização de uma conta
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        self._transacoes_do_dia = []

    @property
    def saldo(self):
        # Propriedade para obter o saldo da conta
        return self._saldo

    @property
    def numero(self):
        # Propriedade para obter o número da conta
        return self._numero

    @property
    def agencia(self):
        # Propriedade para obter a agência da conta
        return self._agencia

    @property
    def cliente(self):
        # Propriedade para obter o cliente associado à conta
        return self._cliente

    @property
    def historico(self):
        # Propriedade para obter o histórico de transações da conta
        return self._historico

    def _verificar_limite_transacoes(self):
        # Verifica se o limite de transações diárias foi atingido
        hoje = datetime.now().date()
        transacoes_hoje = [transacao for transacao in self._transacoes_do_dia if transacao.date() == hoje]
        return len(transacoes_hoje) >= self.MAX_TRANSACTIONS_PER_DAY

    @log_transacao_arquivo
    def sacar(self, valor):
        # Método para realizar um saque na conta
        if self._verificar_limite_transacoes():
            print("\n@@@ Operação falhou! Limite de transações diárias excedido. @@@")

        elif valor > self.saldo:
            print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            self._transacoes_do_dia.append(datetime.now())
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False

    @log_transacao_arquivo
    def depositar(self, valor):
        # Método para realizar um depósito na conta
        if self._verificar_limite_transacoes():
            print("\n@@@ Operação falhou! Limite de transações diárias excedido. @@@")

        elif valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
            self._transacoes_do_dia.append(datetime.now())
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        # Inicialização de uma conta corrente
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        # Método para realizar um saque em uma conta corrente
        if valor > self._limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif len(self._transacoes_do_dia) >= self._limite_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False
    
    def __repr__(self):
        return f"""<{self.__class__.__name__}: ('{self.agencia}', '{self.numero}', '{self.cliente.nome}')>"""

    def __str__(self):
        # Método para representar uma conta corrente como uma string formatada
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data_hora": datetime.now().strftime(" %d/%m/%Y %H:%M"),  # Adiciona data e hora da transação
            }
        )


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        # Propriedade para obter o valor da transação
        pass

    @abstractclassmethod
    def registrar(self, conta):
        # Método abstrato para registrar uma transação em uma conta
        pass


class Saque(Transacao):
    def __init__(self, valor):
        # Inicialização de uma transação de saque
        self._valor = valor

    @property
    def valor(self):
        # Propriedade para obter o valor do saque
        return self._valor

    def registrar(self, conta):
        # Método para registrar um saque em uma conta
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        # Inicialização de uma transação de depósito
        self._valor = valor

    @property
    def valor(self):
        # Propriedade para obter o valor do depósito
        return self._valor

    def registrar(self, conta):
        # Método para registrar um depósito em uma conta
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)



def menu():
    # Função para exibir o menu de opções
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def filtrar_cliente(cpf, clientes):
    # Função para filtrar um cliente por CPF
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    # Função para recuperar a primeira conta associada a um cliente
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    # FIXME: não permite cliente escolher a conta
    return cliente.contas[0]

@log_transacao_arquivo
def depositar(clientes):
    # Função para realizar um depósito
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

@log_transacao_arquivo
def sacar(clientes):
    # Função para realizar um saque
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = float(input("Informe o valor do saque: "))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

@log_transacao_arquivo
def exibir_extrato(clientes):
    # Função para exibir o extrato de uma conta
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['data_hora']} \n{transacao['tipo']}: \n\tValor: R$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

@log_transacao_arquivo
def criar_cliente(clientes):
    # Função para criar um novo cliente
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")

@log_transacao_arquivo
def criar_conta_de_um_cliente_para_o_banco(numero_conta, clientes, contas):
    # Função para criar uma nova conta
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente(numero=numero_conta, cliente=cliente)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")

def listar_contas(contas):
    # Função para listar todas as contas
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    # Função principal
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta_de_um_cliente_para_o_banco(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


main()
