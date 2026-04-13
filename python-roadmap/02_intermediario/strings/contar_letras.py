#len(): conta todos os caracteres, não apenas letras.
frase = input('Digite uma frase: ')
print("Quantidade de caracteres: ", len(frase))

#isalpha(): retorna True apenas para letras
quantidade = sum(1 for c in frase if c.isalpha())
print("Quantidade de letras:", quantidade)

# len(frase.split(): retorna o número de palavras na frase
print("Quantidade de palavras: ", len(frase.split()))

