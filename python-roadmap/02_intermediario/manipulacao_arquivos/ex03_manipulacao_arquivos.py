#Conta quantas linhas existem no arquivo.
with open("cadastro.txt", "r") as f:
    quantidade = sum(1 for _ in f)

print("Quantidade de linhas:", quantidade)

#Ignora linhas vazias
with open("cadastro.txt", "r") as f:
    quantidade = sum(1 for linha in f if linha.strip())

print("Linhas não vazias:", quantidade)