idade=int(input("Digite sua idade: "))

if idade < 0:
    print("Idade inválida")
elif idade <18:
    print("Menor de idade")
elif idade<60:
    print("Adulto")
else:
    print("Idoso")