#Ex04 - Cria uma função 'def dividir (a,b):'
#- Retorne o resultado da divisão
#- Trate erros dentro da função
#- Retorne uma mensagem em vez de quebrar o programa

def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero."
    except TypeError:
        return "Erro: valores inválidos."

# Exemplo de uso
resultado = dividir(10, 2)
print(resultado)