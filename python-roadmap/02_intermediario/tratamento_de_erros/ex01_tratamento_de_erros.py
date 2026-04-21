#Ex01- programa que:
#- Peça dois números
#- Mostre a soma
#- Trate erro caso o usuário digite texto

try:
    num1  = int(input("Digite um numero: "))
    num2 = int(input("Digite outro numero: "))
    soma = num1 + num2
    print(soma)
except ValueError:
    print("Digite um número válido.")


