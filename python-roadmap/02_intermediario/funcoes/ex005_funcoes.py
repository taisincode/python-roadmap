#5: Crie função que receba *kwargs e imprima dados formatados.

def mostrar_dados(**dados):
    for chave,valor in dados.items():
        print(chave,valor)

mostrar_dados(nome="Ana",idade=20,curso="ADS")