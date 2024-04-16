menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Digite o valor a ser depositado: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito de R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso.")
        else:
            print("Valor inválido. Por favor, digite um valor positivo.")

    elif opcao == "s":
        print("Saque")
        valor = float(input("Digite o valor a ser sacado: "))
        if valor > 0 and valor <= limite and numero_saques < LIMITE_SAQUES:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado com sucesso.")
        elif valor > 0 and valor > limite:
            print("Limite excedido. Por favor, digite um valor menor ou igual a R$ 500.00.")
        elif numero_saques >= LIMITE_SAQUES:
            print("Limite de saques diários excedido. Por favor, tente novamente amanhã.")
        elif valor > 0 and valor <= saldo:
            print("Saldo insuficiente. Por favor, verifique seu saldo e tente novamente.")

    elif opcao == "e":
        print("================= Extrato ===================")
        print(extrato)
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "q":
        print("Saindo")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")