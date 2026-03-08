# Crie uma lista com 5 números e mostre o maior.

numeros = [1,2,11,4,5]
print(numeros)

print(max(numeros)) #mostra o maior elemento da lista

#forma com for e if
maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero

print(maior)