numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite +, -, *, /: ")

if operacao == "+":
    print(numero1+numero2)
elif operacao == "-":
    print(numero1-numero2)
elif operacao == "*":
    print(numero1*numero2)
elif operacao == "/":
    if numero2 != 0:
        print(numero1/numero2)
    else:
        print("Divisão por zero não permitida")
else:
     print("Operação inválida")