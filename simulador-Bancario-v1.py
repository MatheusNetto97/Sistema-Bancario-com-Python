import datetime

menu = """
Escolha uma opção abaixo:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

# Variáveis
saldo = 0
limite = 500
extrato = []
numero_saque = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Qual valor será depositado: "))

        if valor > 0:
            saldo += valor
            agora = datetime.datetime.now()
            extrato.append(
                f"{agora.strftime('%Y-%m-%d %H:%M:%S')} - Depósito: R${valor:.2f}")

        else:
            print("Valor impossível de ser depositado")

    elif opcao == "s":
        valor_saque = float(input("Digite o valor que deseja sacar: "))

        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saque = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação não realizada, falta de saldo em sua conta")

        elif excedeu_limite:
            print(
                "Falha na operação, o valor de saque excede o limite de saldo em sua conta")

        elif excedeu_saque:
            print(
                "Impossível realizar saque! Você excedeu o número de saques em sua conta")

        elif valor_saque > 0:
            saldo -= valor_saque
            agora = datetime.datetime.now()
            extrato.append(
                f"{agora.strftime('%Y-%m-%d %H:%M:%S')} - Saque: R${valor_saque:.2f}")
            numero_saque += 1

        else:
            print("Valor inválido!")

    elif opcao == "e":
        print("\n------------EXTRATO------------")
        if not extrato:
            print("Não houve movimentações em sua conta.")
        else:
            for item in extrato:
                print(item)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("---------------------------------")

    elif opcao == "q":
        break

    else:
        print('Opção Inválida')
