#Sets/conjuntos é uma coleção não ordenada e sem elemesntos duplicados.
numeros = {1,2,3,3} #cria conjuntos
print(numeros)

numeros.add(5) #adiciona elemento
print(numeros)

numeros.remove(3) #remove elemento
print(numeros)


a = {1,2,3}
b = {2,3,4,5}

print(a|b) #retorna a união do conjunto 'a' e 'b': {1, 2, 3, 4, 5}

print(a&b) #retornar somente os elementos que os dois conjuntos tem em comum:{2, 3}

print(a-b) #retorna do conjunto 'a' apenas os elementos que não tem no conjunto 'b':{1}

print(a^b) #retorna do conjunto 'a' apenas os elementos que não tem no conjunto 'b' e vice versa