# 1 - Crie um programa que peça um número e diga se é positivo, negativo ou zero.

num = int(input('digite um número: '))

if num == 0:
    print('Zero')
elif num >= 1:
    print('Número positivo')    
else:
    print('Número negativo')    