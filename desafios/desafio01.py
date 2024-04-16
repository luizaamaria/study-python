menu = """ 
============= Sistema Bancário =============

[1] - depositar
[2] - sacar
[3] - extrato
[4] - sair

============================================

=> Digite a opção desejada:  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        deposito = float(input("Digite o valor do depósito: "))

        if deposito <= 0:
            print("Valor inválido, tente novamente!")
            continue
        
        saldo += deposito

        print(f"Depósito: R$ {deposito:.2f}")

    elif opcao == "2":
        saque = float(input("Digite o valor do saque: "))

        if saque > saldo:
            print("Saldo insuficiente!")
            continue

        if numero_saques >= LIMITE_SAQUES:
            print("Limite de saques atingido!")
            continue

        saldo -= saque
        numero_saques += 1
        print(f"Saque: R$ {saque:.2f}")

    elif opcao == "3":
        print(
            "Extrato Bancário\n"
            f"Saldo Atual: R$ {saldo:.2f}"
            f"\nSaques realizados: {numero_saques}"
        )

    elif opcao == "4":
        print("Saindo do sistema...")
        break
    
    else:
        print("Opção inválida , selecione uma opção válida!")