#5- Faça um programa que conte letras únicas de uma palavra usando set.


palavra = 'programação'

# transforma a palavra em um conjunto (set)
# o set separa as letras e remove as repetidas
letras_unicas = set(palavra)


print("Letras únicas:", letras_unicas)

# len() conta quantos elementos existem no conjunto
# ou seja, quantas letras únicas a palavra possui
print("Quantidade:", len(letras_unicas))