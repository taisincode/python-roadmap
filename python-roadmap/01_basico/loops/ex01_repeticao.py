# 1 - Faça um programa que mostre números de 1 a 100.

# primeiro exemplo:
for i in range (0,100):
    print (i + 1)
    
# segundo exemplo: (o código fica mais legível, não precisa de cálculo extra)
for i in range(1, 101):
    print(i)
    
# Terceiro exemplo: (Isso imprime todos os números quebrando linha.)
print(*range(1, 101), sep="\n")