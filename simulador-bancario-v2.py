import datetime
from faker import Faker
import textwrap

fake = Faker()
usuarios = []
contas_correntes = []


def menu():
    menu = """
    Bem vindo ao sistema bancário!

    Digite a sua opção desejada:

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    [n] Novo usuário
    [nc] Numero de Contas
    [lc] Listar contas
    """
    return input(textwrap.dedent(menu))


# Função para criar um usuário com nome, data de nascimento, CPF e endereço
def criar_usuario(usuarios):
    cpf = input("Digite o CPF:")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n ====Usuário já cadastrado!====")
        return

    nome = input("informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input(
        " informe o endereço (logadouro, nº, bairo, cidade/estado)")

    usuarios.append({"nome:": nome, "data_nascimento": data_nascimento,
                    "cpf": cpf, "endereco": endereco})

    print("==== Usuario criado com sucesso!====")


def filtrar_usuario(cpf, usuarios):
    usuario_filtrados = [
        usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrados[0] if usuario_filtrados else None

# Função para criar uma conta corrente para um usuário


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n====Conta Criada com Sucesso!====")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\n==== Usuario não encontrado, fluxo de criação de conta encerrado!====")


# Função para realizar um saque
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n===operação falhou, voce nao possui saldo suficiente===")

    elif excedeu_limite:
        print("\n===Operação falhou, valor do saque exede o limite===")

    elif excedeu_saque:
        print("\n===Operação falhou, ultrapassou a quantidade maxima de saque===")

    elif valor > 0:
        saldo -= valor
        extrato += f"SAQUE:\t\tR$ {valor: .2f}\n"
        numero_saques += 1
        print("\n===Saque realizado com sucesso !===")

    else:
        print('\n===Valor inválido===')

    return saldo, extrato, excedeu_saldo, excedeu_limite, excedeu_saque


# Função para realizar um depósito
def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        print(f"Deposito: R$:{valor: .2f}")
        print("\n====Deposito feito com sucesso====")
    else:
        print("\n====Operação Falhou====")

    return saldo, extrato


# Função para exibir extrato
def exibir_extrato(saldo, *, extrato):

    print("\n=========EXTRATO=========")
    print("Nao foram realizados movimentações." if not extrato else extrato)
    print(f"\nSaldo R$:{saldo: .2f}")
    print("===========================")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agencia: {conta["agencia"]}
            C/C: {conta["numero_conta"]}
            Titular: {conta["usuario"]["nome"]}
            """
        print("=" * 100)
        print(textwrap.dedent(linha))


# Lista para armazenar os usuários
usuarios = []

# Lista para armazenar as contas
contas_correntes = []

# Exemplo de uso das funções


def main():
    LIMITE_SAQUE = 5
    AGENCIA = "0001"

    saldo = 0
    limite = 1000
    extrato = ""
    numero_saque = 0
    usuario = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "c":
            # Código para criar contas
            pass

        elif opcao == "d":
            valor = float(input("Qual valor será depositado: "))

            saldo, extrato = deposito(saldo, valor, extrato)

            if valor > 0:
                agora = datetime.datetime.now()
                extrato.append(
                    f"{agora.strftime('%Y-%m-%d %H:%M:%S')} - Depósito: R${valor:.2f}")
            else:
                print("\n====Operação Falhou====")

        elif opcao == "s":
            valor_saque = float(input("Digite o valor que deseja sacar: "))

            saldo, extrato, excedeu_saldo, excedeu_limite, excedeu_saque = saque(
                saldo=saldo,
                valor=valor_saque,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saque,
                limite_saques=LIMITE_SAQUE
            )

            if excedeu_saldo:
                print("\n===Operação não realizada, falta de saldo em sua conta===")

            elif excedeu_limite:
                print(
                    "\n===Falha na operação, o valor de saque excede o limite de saldo em sua conta===")

            elif excedeu_saque:
                print(
                    "\n===Impossível realizar saque! Você excedeu o número de saques em sua conta===")

            elif valor_saque > 0:
                agora = datetime.datetime.now()
                extrato.append(
                    f"{agora.strftime('%Y-%m-%d %H:%M:%S')} - Saque: R${valor_saque:.2f}")
                numero_saque += 1

            else:
                print("Valor inválido!")

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "q":
            break

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
            pass

        elif opcao == "lc":
            listar_contas(contas_correntes)

        elif opcao == "n":
            criar_usuario(usuarios)
            pass

        else:
            print('Opção Inválida')


if __name__ == "__main__":
    from faker import Faker
    fake = Faker()
    main()
