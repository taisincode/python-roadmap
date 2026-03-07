# 2 - Faça um sistema que verifique se uma pessoa pode votar (idade ≥ 16).

idade = int(input('Digite a sua idade: '))

if idade >= 16:
    print('Você já é maior de idade e tem o direito de votar."')
else:
     print("Você ainda é menor de idade. Espere atingir a maioridade para exercer esse direito.")