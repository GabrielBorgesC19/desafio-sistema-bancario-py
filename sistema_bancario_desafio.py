saldo = 0
limite = 500
numero_saques = 0
limite_saque = 3
extrato = ""

menu = """
          ========== MENU =========
            
            1 - Depósito
            2 - Saque
            3 - Exibir extrato

            Selecione uma opção: """
          
while True:


    opcao = int(input(menu)) 
    print()

    if opcao == 1:
        
        valor_deposito = float(input("Digite o valor do deposito: "))
        saldo += valor_deposito
        extrato += f"Deposito: R$ +{valor_deposito:.2f}\n"
        print(f"Deposito realizado com sucesso! Seu saldo e de R${saldo:.2f}")

    elif opcao == 2:

        
        valor_saque = float(input("Digite o valor do saque: "))

        excedeu_saldo = valor_saque > saldo
        excedeu_limite = valor_saque > limite
        excedeu_saques = numero_saques >= limite_saque
        valor_nulo_negativo = valor_saque <= 0

        if valor_nulo_negativo:

            print("Valor invalido, tente novamente...")
        
        elif excedeu_saldo:
            
            print(f"Saldo insuficiente! Saldo atual R${saldo:0.2f}")

        elif excedeu_saques:
            print("Saques excedidos.")

        else: 

            if valor_saque <= limite:

                numero_saques += 1
                saldo -= valor_saque 
                extrato += f"Saque: R$ -{valor_saque:.2f}\n"
                print(f"Saque realizado com sucesso, seu saldo e de: R${saldo:0.2f}")

            elif excedeu_limite:

                print("O limite de saque eh 500, tente novamente...")

    elif opcao == 3:
         print("==========EXTRATO==========\n")
         print("Nao foram realizadas movimentacoes. " if not extrato else extrato)
         print(f"Seu saldo atual: R${saldo:.2f}\n")
         print("===========================")