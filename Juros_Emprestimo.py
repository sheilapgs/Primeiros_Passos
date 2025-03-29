valor = float(input("Digite o vaçor do emprestimo: "))
porcentagem = float(input("Digite a porcetagem: "))
parcelas = int(input("Digite em quantas vezes você deseja parcelar: "))
valor_juros = (valor*porcentagem)/100

if valor_juros:
    resultado = (valor_juros+valor)/parcelas

print("Você pagará ", parcelas, " vezes de R$", resultado, " reais" )