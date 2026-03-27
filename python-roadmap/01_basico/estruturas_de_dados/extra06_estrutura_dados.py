#Exercícios de Estruturas de Dados (nível progressivo)
#Exercício 6 


#Faça um programa que:
##1. peça 10 números
##2. armazene em uma lista
##3. mostre apenas os números únicos usando set.

numeros = []
contador = 0

while contador < 10:
    num = int(input('Digite um número inteiro: '))
    numeros.append (num)
    contador += 1

unicos = set(numeros)

print(unicos)



