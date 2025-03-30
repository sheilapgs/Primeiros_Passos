ano_atual = int(input("Informe o ano atual: "))
ano_nasc = int(input("Informe o ano de nascimento: "))
idade_atual = ano_atual - ano_nasc

if idade_atual >= 18:
    print ("Tem", idade_atual, "anos, portanto já alcançou a maioridade.")
else:
    print("Tem", idade_atual, "anos e não alcançou a maior idade ainda.")

    

