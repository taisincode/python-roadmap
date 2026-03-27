#Exercícios de Estruturas de Dados (nível progressivo)
#Exercício 5 — Set + lógica (nível mais difícil)


#Peça ao usuário duas palavras.O programa deve mostrar:
##1. Letras que aparecem nas duas palavras.
##2. Letras que aparecem apenas na primeira palavra.
##3. Letras que aparecem apenas na segunda palavra.

import unicodedata
import re

def normalizar(texto):
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    texto = re.sub(r'[^a-z0-9]', '', texto)
    return texto

# Entrada
palavra1 = input('Digite uma palavra: ')
palavra2 = input('Digite mais uma palavra: ')

# Normalização
p1 = normalizar(palavra1)
p2 = normalizar(palavra2)

# Sets
set1 = set(p1)
set2 = set(p2)

# Interseção
comum = set1 & set2

print('Letras que aparecem nas duas palavras:')
print(comum)

# Diferença 1
print('Letras que aparecem apenas na primeira palavra:')
diferenca1 = set1 - set2
print(diferenca1)

# Diferença 2
print('Letras que aparecem apenas na segunda palavra:')
diferenca2 = set2 - set1
print(diferenca2)
