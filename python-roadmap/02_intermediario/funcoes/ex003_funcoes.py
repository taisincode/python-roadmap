#3: Crie função com parâmetro padrão.

#Exemplo simples
def saudacao(nome="Visitante"):
    print(f"Olá, {nome}!")

saudacao("Ana")
saudacao()

#Exemplo com cálculo
def somar(a, b=0):
    return a + b

print(somar(5, 3))
print(somar(5))     # (usa o padrão b=0)

#exemplo com lista
def adicionar_item(lista=None):
    if lista is None:
        lista = []
    lista.append(1)
    return lista

print(adicionar_item())
print(adicionar_item([5]))