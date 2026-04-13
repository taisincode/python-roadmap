#palíndromo: é uma palavra, frase ou número que pode ser lido da mesma forma de trás para frente.
palavra = input("Digite uma palavra: ")

if palavra==palavra[::-1]:
    print("É palíndromo")
else:
    print("Não é palíndromo")