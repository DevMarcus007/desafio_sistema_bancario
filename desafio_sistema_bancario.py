menu = """
Escolha a operação desejada:

[1] Efetuar Deposito
[2] Efetuar Saque
[3] Emitir Extrato
[0] Sair


"""


saldo = 0
qtd_saques = 0
limite = 500
extrato=[]

LIMITES_SAQUES = 3

print('\n\nBem vindo ao Banco DIO!')
while True:
    opcao = input(menu)

    if opcao == '1':
        while True:
            valor_deposito = input('\nInforme o valor para depósito: ')
            if ',' in valor_deposito:
                    valor_deposito = valor_deposito.replace(',', '.')
            if not valor_deposito.isalpha():
                valor_deposito = float(valor_deposito)
                if valor_deposito > 0:
                    saldo += valor_deposito
                    extrato.append(f"Depósito: R$ {valor_deposito:.2f}")
                    print("\nOperação de DEPÓSITO realizada com sucesso!\n")
                    break
            else:
                print('\nValor de depósito informado é inválido. Digite o valor')

    elif opcao == '2':
        if  qtd_saques < LIMITES_SAQUES:
            while True:
                valor_saque = input('\nInforme o valor para saque: ')
                if ',' in valor_saque:
                        valor_saque = valor_saque.replace(',', '.')
                if not valor_saque.isalpha():
                    valor_saque = float(valor_saque)
                    if valor_saque > 0 and valor_saque <= 500:
                        if valor_saque > saldo:
                            print('\nValor indisponível para saque.')
                            break
                        else:
                            saldo -= float(valor_saque)
                            extrato.append(f"Saque: R$ {valor_saque:.2f}")
                            qtd_saques += 1
                            print("\nOperação de SAQUE realizada com sucesso!\n")
                            break
                    else:
                        print('\nLimite de valor por saque é de R$ 500.00')
                else:
                    print('\nValor de saque informado é inválido. Digite o valor')
        else:
            print('\nLimite diário de saques já atingido.')

    elif opcao == '3':
        print("\n********** EXTRATO **********")
        print("Não foram realizadas movimentações." if not extrato else "\n".join([item for item in extrato]))
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n*****************************")

    elif opcao == '0':
        print('\nObrigado por utilizar o Banco DIO')
        break
    else:
         print('\nOpção digitáda é inválida.')
