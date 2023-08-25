import textwrap



def menu():
    menu = """\n\n
            Escolha a operação desejada:

            [1] Efetuar Deposito
            [2] Efetuar Saque
            [3] Emitir Extrato
            [4] Nova Conta
            [5] Listar Contas
            [6] Novo Usuario
            [0] Sair\n
            """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    saldo += valor
    extrato.append(f"Depósito: R$ {valor:.2f}")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    saldo -= float(valor)
    extrato.append(f"Saque: R$ {valor:.2f}")
    numero_saques += 1
    return saldo, extrato, numero_saques

def visualizar_extrato(saldo, /, *, extrato):
    print("\n********** EXTRATO **********")
    print("Não foram realizadas movimentações." if not extrato else "\n".join([item for item in extrato]))
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n*****************************")

def criar_usuario(usuarios):
    while True:
        cpf = input('Informe o CPF(somente numeros): ')
        usuario = filtrar_usuario(cpf, usuarios)
        if usuario:
            print('Já existe usuário cadastrado com este usuário.')
        else:
            break
    nome = input('Informe o nome completo: ')
    data_nascimento = input('Informe a data de nascimento (dd-mm-aaaa): ')
    logradouro = input('Informe o logradouro: ')
    numero = input('Informe o número da residência: ')
    bairro = input('Informe o bairro: ')
    cidade = input('Informe a cidade: ')
    uf = input('Informe a UF do Estado: ')

    usuarios.append({'nome':nome, 'data_nascimento':data_nascimento, 'cpf':cpf, 'endereco':f'{logradouro}, {numero} - {bairro} - {cidade}/{uf}'})

    print('=== Usuário criado com sucesso! ===')

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def abrir_conta(agencia, numero_conta, usuarios):
    cpf = input('Informe o CPF do usuario: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\nConta criada com sucesso!')
        return {'agencia':agencia, 'numero_conta':numero_conta, 'usuario':usuario}

    print('\nUsuario não encontrado.')

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
                Agência:\t{conta['agencia']}
                C/C:\t\t{conta['numero_conta']}
                Titular:\t{conta['usuario']['nome']}
                """
        print('='*100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 0
    usuarios = []
    contas = []
    
    while True:
        opcao = menu()

        if opcao == '1':
            while True:
                valor_deposito = input('\nInforme o valor para depósito: ')
                if ',' in valor_deposito:
                        valor_deposito = valor_deposito.replace(',', '.')
                if not valor_deposito.isalpha():
                    valor_deposito = float(valor_deposito)
                    if valor_deposito > 0:
                        saldo, extrato = depositar(saldo, valor_deposito, extrato)
                        
                        print("\nOperação de DEPÓSITO realizada com sucesso!\n")
                        break
                else:
                    print('\nValor de depósito informado é inválido. Digite o valor')

        elif opcao == '2':
            if  numero_saques < LIMITE_SAQUES:
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
                                saldo, extrato, numero_saques = sacar(
                                    saldo=saldo,
                                    valor=valor_saque,
                                    extrato=extrato,
                                    limite=limite,
                                    numero_saques = numero_saques,
                                    limite_saques = LIMITE_SAQUES,
                                )
                                print("\nOperação de SAQUE realizada com sucesso!\n")
                                break
                        else:
                            print('\nLimite de valor por saque é de R$ 500.00')
                    else:
                        print('\nValor de saque informado é inválido. Digite o valor')
            else:
                print('\nLimite diário de saques já atingido.')
        
        elif opcao == '3':
            visualizar_extrato(saldo, extrato=extrato)

        elif opcao =='4':
            numero_conta = len(contas)+1
            conta = abrir_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == '5':
            listar_contas(contas)

        elif opcao == '6':
            criar_usuario(usuarios)

        elif opcao == '0':
            print('\nObrigado por utilizar o Banco DIO')
            break
        else:
            print('\nOpção digitáda é inválida.')


main()




