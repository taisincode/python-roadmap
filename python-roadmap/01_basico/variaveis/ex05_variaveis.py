# 5 - O que acontece se tentar somar string com número?
"""
texto = "Python"
numero = 10

resultado = texto + numero # Isso gera erro, porque Python não permite somar str com int diretamente


#Exibiria o resultado na tela, mas o código nem chega aqui por causa do erro
print(resultado)
"""

# O erro acontece porque "texto" é uma string
# e "numero" é um inteiro.
# Em Python, tipos diferentes não podem ser somados diretamente.

texto = "Python"
numero = 10

# Convertendo o número para string antes da soma
str_numero = str(numero)

# Agora a soma é permitida, porque os dois valores são strings
resultado = texto + str_numero

print(resultado)