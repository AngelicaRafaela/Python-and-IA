import textwrap  # Importa o módulo textwrap para formatar o texto do menu.

def menu():
    # Define a função menu, que exibe as opções do menu e retorna a escolha do usuário.
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo Usuário
    [nc]\tNova Conta
    [lc]\tListar Contas
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))  # Usa textwrap.dedent para formatar o texto do menu.

def depositar(saldo, valor, extrato, /):
    # Define a função depositar, que realiza uma operação de depósito.
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"  # Atualiza o extrato com a operação de depósito.
        print("\nDepósito concluído com sucesso!")  # Mensagem de sucesso
    else:
        print("\nOops! O valor informado é inválido.")  # Mensagem de erro

    return saldo, extrato  # Retorna o saldo e o extrato atualizados.

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    # Define a função sacar, que realiza uma operação de saque.
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOops! Saldo insuficiente para realizar o saque.")  # Mensagem de erro

    elif excedeu_limite:
        print("\nOops! O valor do saque excede o limite disponível.")  # Mensagem de erro

    elif excedeu_saques:
        print("\nOops! Você já realizou o número máximo de saques permitidos hoje.")  # Mensagem de erro

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"  # Atualiza o extrato com a operação de saque.
        numero_saques += 1
        print("\nSaque concluído com sucesso!")  # Mensagem de sucesso

    else:
        print("\nOops! O valor informado é inválido.")  # Mensagem de erro

    return saldo, extrato  # Retorna o saldo e o extrato atualizados.

def exibir_extrato(saldo, /, *, extrato):
    # Define a função exibir_extrato, que exibe o extrato bancário do usuário.
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)  # Verifica se há movimentações no extrato.
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")  # Exibe o saldo atual.
    print("==========================================")

def criar_usuario(usuarios):
    # Define a função criar_usuario, que cria um novo usuário.
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)  # Verifica se o usuário já existe.

    if usuario:
        print("\nOops! Já existe um usuário com esse CPF!")  # Mensagem de erro
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})  # Adiciona o novo usuário à lista de usuários.

    print("\nUsuário criado com sucesso!")  # Mensagem de sucesso

def filtrar_usuario(cpf, usuarios):
    # Define a função filtrar_usuario, que verifica se um usuário já existe com base no CPF.
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    # Define a função criar_conta, que cria uma nova conta corrente.
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)  # Verifica se o usuário existe.

    if usuario:
        print("\nConta criada com sucesso!")  # Mensagem de sucesso
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}  # Retorna os detalhes da conta.

    print("\nOops! Usuário não encontrado, fluxo de criação de conta encerrado!")  # Mensagem de erro

def listar_contas(contas):
    # Define a função listar_contas, que exibe todas as contas correntes.
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))  # Usa textwrap.dedent para formatar a linha.

def main():
    # Função principal que gerencia o fluxo do programa.
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []  # Lista para armazenar os usuários.
    contas = []  # Lista para armazenar as contas correntes.

    while True:
        opcao = menu()  # Exibe o menu e obtém a opção do usuário.

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)  # Realiza o depósito.

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )  # Realiza o saque.

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)  # Exibe o extrato bancário.

        elif opcao == "nu":
            criar_usuario(usuarios)  # Cria um novo usuário.

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)  # Adiciona a nova conta à lista de contas correntes.

        elif opcao == "lc":
            listar_contas(contas)  # Lista todas as contas correntes.

        elif opcao == "q":
            break  # Sai do loop e encerra o programa.

        else:
            print("Oops! Operação inválida, por favor selecione novamente a operação desejada.")  # Mensagem de erro

main()  # Chama a função principal para iniciar o programa.
