#2: Crie função que receba lista e retorne soma.


def somar_lista(lista):
    total = 0
    for numero in lista:
        total += numero
    return total

print (somar_lista([1,2,3,4,5]))
