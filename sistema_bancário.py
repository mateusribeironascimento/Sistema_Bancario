menu = f"""{'-' * 40}
{'SISTEMA BANCÁRIO':^40}
{'-' * 40}
[1] Saque
[2] Deposito
[3] Extrato
[4] Sair
{'-' * 40}
SUA OPÇÃO: """

saldo = 1000
limite = 500
extrato_saques = []
extrato_depositos = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    print('-' * 40)

    if opcao == '1':
        print(f'{"SAQUE":^40}')
        saque = float(input('Quanto você deseja sacar? R$ '))
        if saque > limite:
            print('O valor máximo para saques é de R$500.00.')
        elif saque < 0:
            print('Não é possível sacar um valor negativo.')
        elif numero_saques == LIMITE_SAQUES:
            print('Você já atingiu o limite de três'
                  '\nsaques diários.')
        elif saque > saldo:
            print('O seu saldo é inferior ao saque desejado.')
        else:
            numero_saques += 1
            saldo -= saque
            extrato_saques.append(saque)
            print(f'Você sacou R${saque:.2f}.')

    elif opcao == '2':
        print(f'{"DEPOSITO":^40}')
        deposito = float(input('Quanto você deseja depositar? R$ '))
        if deposito < 0:
            print('Não é possivel depositar um valor negativo.')
        else:
            saldo += deposito
            extrato_depositos.append(deposito)

    elif opcao == '3':
        print(f'{"EXTRATO":^40}')
        print('SAQUES')
        for i in extrato_saques:
            print(f'R$ {i:.2f}')
        print('DEPOSITOS:')
        for i in extrato_depositos:
            print(f'R$ {i:.2f}')

    elif opcao == '4':
        print(f'{"Obrigado pela preferência.":^40}')
        break

    else:
        print('Operação inválida, por favor selecione'
              '\nnovamente a operação desejada')

