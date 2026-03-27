import unicodedata
import re

# funções
def normalizar(texto):
    """
         Normaliza um texto removendo acentos, convertendo para minúsculas
    e eliminando caracteres não alfanuméricos.

    Parâmetros:
        texto (str): texto a ser normalizado

    Retorna:
        str: texto normalizado
    """
    texto = texto.lower()
    texto = unicodedata.normalize('NFD', texto)
    texto = ''.join(c for c in texto if unicodedata.category(c) != 'Mn')
    texto = re.sub(r'[^a-z0-9]', '', texto)
    return texto
help(normalizar)

def soma(a, b): return a + b


def sub(a, b): return a - b


def mult(a, b): return a * b


def div(a, b): return a / b

# dicionário
operacoes = {
    'soma': soma,
    'subtracao': sub,
    'multiplicacao': mult,
    'divisao': div
}
# execução
while True:
    print("\nEscolha a operação ou digite 'sair':")
    resposta = input("'Soma', 'Subtração', 'Divisão', 'Multiplicação' \n")

    operacao = normalizar(resposta)

    if operacao == 'sair':
        print("Encerrando calculadora...")
        break

    if operacao not in operacoes:
        print("Operação inválida. Tente: soma, subtração, multiplicação ou divisão.")
        continue

    try:
        num1 = float(input('num1 = '))
    except ValueError:
        print("Digite apenas números válidos")
        continue

    try:
        num2 = float(input('num2 = '))
    except ValueError:
        print("Digite apenas números válidos")
        continue

    try:
        resultado = operacoes[operacao](num1, num2)
        print("Resultado:", resultado)
    except ZeroDivisionError:
        print("Erro: divisão por zero")


