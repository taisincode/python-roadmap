#Exercícios de Estruturas de Dados (nível progressivo)
#Exercício 1 — Lista (nível básico)

#Crie uma lista com 5 números digitados pelo usuário. Depois:
##1. Mostre todos os números digitados.
##2. Mostre o maior número.
##3. Mostre o menor número.

numeros = []

for i in range(5):
    numero = input('Digite um número inteiro: ')
    numeros.append(numero)
print(numeros)

menor = numeros[0]

for numero in numeros:
    if numero < menor:
        menor = numero
print(menor)


maior = numeros[0]

for numero in numeros:
    if numero > maior:
        maior = numero
print(maior)