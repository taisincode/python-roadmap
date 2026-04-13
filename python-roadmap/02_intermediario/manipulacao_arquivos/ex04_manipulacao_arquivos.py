#sistema simples de login que ler usuário e senha de um arquivo.
usuario_digitado = input("Usuário: ")
senha_digitada = input("Senha: ")

login_valido = False

with open("usuarios.txt", "r") as f:
    for linha in f:
        usuario, senha = linha.strip().split(":")

        if usuario == usuario_digitado and senha == senha_digitada:
            login_valido = True
            break

if login_valido:
    print("Login realizado com sucesso!")
else:
    print("Usuário ou senha incorretos.")