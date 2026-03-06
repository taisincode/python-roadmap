# 2 - Crie um programa que peça um número inteiro ao usuário, verifique se ele é par ou ímpar e mostre o resultado na tela.

num = int(input('Digite um número: '))

resultado = num // 2

if resultado == 0:
    print('o número é par.')
else:
    print('O número é impar.')    