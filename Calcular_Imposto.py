
preco = float(input("Digite o valor do produto: "))
porcentagem = float(input("Digite a porcentagem paga sobre o preco: "))

if porcentagem:
    resultado = (preco*porcentagem)/100

print("Você vai pagar: US$", porcentagem, " de imposto. ") 
