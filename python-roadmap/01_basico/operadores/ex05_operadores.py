# 5 - Crie um programa que peça um número e verifique se ele está entre 10 e 50. Mostre uma mensagem informando se está ou não no intervalo.

num = int(input('Digite um número inteiro: '))

if num >= 10 and num <= 50:
    print('O número está no intervalo permitido.')
else: 
    print('O número nâo está no intervalo permitido.')