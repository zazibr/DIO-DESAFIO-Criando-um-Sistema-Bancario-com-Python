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

    if opcao == 'd':   # depositar
        valor = float(input("Digite o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou: O valor informado é inválido.")

    elif opcao == 's': # sacar
        valor = float(input("Digite o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques == LIMITE_SAQUES

        if excedeu_saldo:
            print( "Operação falhou: Você não tem saldo sulficiente.")

        elif excedeu_limite:
            print( "Operação falhou: Você do saque excede o limite.")

        elif excedeu_saques:
            print( "Operação falhou: Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque : {valor:.2f}\n"
            numero_saques += 1

        else:
            print( "Operação falhou: O Valor informado é inválido.")


    elif opcao == 'e': # extrato
        print( "Extrato")
        print("\n********** EXTRATO ********** ")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print("\n****************** ********** ")

    elif opcao == 'q': # Sair
        break
    else:
        print( "Operação inválida, por favor selecione novamente a operação desejada.")
