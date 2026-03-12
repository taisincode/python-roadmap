#Exercícios de Estruturas de Dados (nível progressivo)
#Exercício 3 — Tupla + lógica (nível intermediário)


#Crie uma tupla com os dias da semana. Depois:
##1. Peça ao usuário para digitar um número de 1 a 7.
##2. Mostre qual é o dia correspondente.

dias = ('SEGUNDA-FEIRA','TERÇA-FEIRA','QUARTA-FEIRA','QUINTA-FEIRA','SEXTA-FEIRA','SÁBADO','DOMINGO')

numero = int(input('Digite um número de 1 a 7: '))

print(dias[numero - 1])