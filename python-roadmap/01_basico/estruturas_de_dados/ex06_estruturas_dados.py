#6- Faça um programa que receba 5 nomes e armazene em lista.

nomes = []

for i in range(5):# repete 5 vezes
    nome = input('Digite o nome: ')
    nomes.append(nome)# adiciona no final da lista

print(nomes)