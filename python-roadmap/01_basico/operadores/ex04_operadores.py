# 4 - Crie um programa que peça o valor de um produto e peça a idade do cliente. Se a pessoa tiver 60 anos ou mais, aplique 20% de desconto, caso contrário aplique 10% de descontov e mostre o valor final.

valor_original = float(input('Digite o valor do produto: '))
idade = int(input('Digite a idade do cliente: '))

if idade >= 60: 
    valor_com_desconto = valor_original - (valor_original * (20/100))
    print('Valor final: ', valor_com_desconto)
else:
        valor_com_desconto = valor_original - (valor_original * (10/100))
        print('Valor final: ', valor_com_desconto)