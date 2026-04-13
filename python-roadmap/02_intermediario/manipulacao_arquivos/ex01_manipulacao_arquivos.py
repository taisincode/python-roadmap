#Ler o arquivo e mostra apenas o primeiro nome.
with open ("cadastro.txt", "r") as f:
    print(f.readline())