massa = float(input("Digite a massa(kg): "))
altura = float(input("Digite a altura (m): "))
imc = massa/(altura**2)

if 18.5<=imc<=24.9:
    print("SIM, você está dentro da sua faixa de peso ideal.")
else:
    print("Você NÃO está dentro da sua faixa de peso ideal")
