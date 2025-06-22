# Começar com as váriáveis

saldo = 0.0
extrato = ""
saques = 0
Limite_Saque = 500.00
Saque_Diario = 3

# Laço principal

print("\n====== BEM VINDO(A)! ======\n")

while True:
    print("========== MENU ==========")
    print("[d]eposito")
    print("[s]aque")
    print("[e]xtrato")
    print("[q] sair")

# Lógica da operação

    operacao = input("Escolha uma opção: ")

    if operacao == 'd':
        valor = float(input("Digite o valor que deseja depositar: "))

        if valor >0:
            saldo += valor
            extrato += f"Depósito: R${valor:.2f}\n"
            print("\nSeu depósito foi concluído com sucesso!\n")
        else:
            print("\nValor inválido. Informe um valor positivo, por favor.\n")


    elif operacao == 's':
        sacar = float(input("Digite o valor que deseja sacar: "))

        if saques >=3:
            print("\nLimite de saques diário atingido, tente novamente mais tarde!\n")
        elif sacar > saldo:
            print ("\nSaldo insuficiente.\n")
        elif sacar > 500:
            print("\nLimite máximo de saque R$ 500.00 por saque.\n")
        elif sacar >0:
            saldo -= sacar
            extrato += f"Saque: R${sacar:.2f}\n"
            saques += 1
            print("\nSaque concluído com sucesso!")
            print(f"Você já fez {saques} de {Saque_Diario} saques hoje.\n")
        else:
            print("\nValor inválido.\n")
          
    elif operacao == 'e':
        if saldo == 0:
            print("\nSeu saldo está zerado.\n")
        else:
            print(f"Saldo atual: R${saldo:.2f}\n")
    
    elif operacao == 'q':
        print("\nEncerrando a sessão...")
        print("Obrigado(a) por usar nossos serviços, volte sempre!\n")
        break

    else:
        print("Opção Inválida!")