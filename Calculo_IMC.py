massa = float(input("Digite o peso(kg): "))
altura = float(input("Digite a altura (m): "))
imc = massa/(altura**2)


if imc <17:
    print("Muito abaixo do peso")
elif 17<=imc<=18.5:
    print("Abaixo do peso")
elif 18.5<imc<=24.9:
    print("Peso ideal")
elif 25>=imc<=29.9:
    print("Sobrepeso")
elif 30<=imc<=34.9:
    print("Obesidade grau 1")
elif 35<=imc<=39.9:
    print("Obesidade grau 2")
else:
    print("Obesidade mórbida")
