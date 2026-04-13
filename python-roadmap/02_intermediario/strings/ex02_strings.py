#Pedir frase e contar quantas vezes uma letra especifica aparece.
#Usando count() e Ignorando maiúsculas/minúsculas
frase = input("Digite uma frase: ").lower()
letra = input("Digite a letra que deseja contar: ").lower()

quantidade = frase.count(letra)
print("Quantidade:", quantidade)

#usando for
frase = input("Digite uma frase: ").lower()
letra = input("Digite a letra: ").lower()

contador = 0
for c in frase:
    if c == letra:
        contador += 1

print("Quantidade:", contador)

#Conta várias letras ao mesmo tempo
frase = input("Digite uma frase: ").lower()

print("a:", frase.count("a"))
print("e:", frase.count("e"))
print("i:", frase.count("i"))
print("o:", frase.count("o"))
print("u:", frase.count("u"))