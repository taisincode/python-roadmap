# 3 - Crie um programa que peça duas notas de um aluno, calcule a média e mostre aprovado se a média for maior ou igual a 7, caso contrário mostre reprovado.

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('Nota 1: ', nota1)
    print('Nota 2: ', nota2)
    print('Média: ', media)
    print('Aluno aprovado')
else:  
    print('Nota 1: ', nota1)
    print('Nota 2: ', nota2)
    print('Média: ', media)
    print('Aluno reprovado')