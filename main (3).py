saldo = 100
qtd_saques = 0
qtd_depositos = 0
saques = []
depositos = []

def deposito(valor):
    global saldo, qtd_depositos
    saldo += valor
    qtd_depositos += 1
    depositos.append(valor)
    return "|*| depósito realizado com sucesso!!\n"

def saque(valor):
    global saldo, qtd_saques
    if qtd_saques < 3:
        if valor <= saldo and valor <= 500:
            saldo -= valor
            qtd_saques += 1
            saques.append(valor)
            return "|*| saque realizado com sucesso!!\n"
        else:
            return "|*| saldo insuficiente ou limite de saque excedido!\n"
    else:
        return "|*| limite de saques excedido!\n"

def extrato():
    print("*_" * 20)
    print("EXTRATO BANCÁRIO do usuário 325")
    print("--" * 20)
    if qtd_depositos > 0:
        for valor in depositos:
            print(f"@depósito@: R$ {valor:.2f}\t--/--/----")
    if qtd_saques > 0:
        for valor in saques:
            print(f"@saque@: R$ {valor:.2f}\t--/--/----")
    if qtd_saques == 0 and qtd_depositos == 0:
        print("|*| não há movimentações para exibir!")
    print("-" * 30)
    print(f"@saldo atual@: R$ {saldo:.2f}\n")

while True:
    print("*_" * 20)
    print("|*| BANCO DO CÓDIGO - MENU PRINCIPAL |*|")
    print("[1] depósito")
    print("[2] saque")
    print("[3] extrato")
    print("[4] sair")
    print("--"*20)
    opcao = int(input("[*] escolha uma opção: "))
    if opcao == 1:
        valor = float(input("[*]digite o valor do depósito: "))
        print(deposito(valor))
    elif opcao == 2:
        valor = float(input("[*]digite o valor do saque: "))
        print(saque(valor))
    elif opcao == 3:
        extrato()
    elif opcao == 4:
        break
    else:
        print("|*| opção inválida!!")
