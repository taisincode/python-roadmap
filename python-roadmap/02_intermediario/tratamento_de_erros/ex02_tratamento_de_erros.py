try:
    numero = float(input('Digite um número: '))

    inverso = 1 / numero
    print(inverso)

except ZeroDivisionError:
    print("Não é possível calcular o inverso de zero.")
except ValueError:
    print("Entrada inválida.")