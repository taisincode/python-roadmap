def carregar_usuarios():
    usuarios = {}

    try:
        with open("usuarios.txt", "r") as f:
            for linha in f:
                if ":" in linha:
                    usuario, senha = linha.strip().split(":")
                    usuarios[usuario] = senha
    except FileNotFoundError:
        pass  # cria vazio se não existir

    return usuarios


def salvar_usuario(usuario, senha):
    with open("usuarios.txt", "a") as f:
        f.write(f"{usuario}:{senha}\n")


def cadastrar():
    usuarios = carregar_usuarios()

    usuario = input("Novo usuário: ").strip()
    senha = input("Nova senha: ").strip()

    # validações
    if not usuario or not senha:
        print("Usuário e senha não podem ser vazios.")
        return

    if usuario in usuarios:
        print("Usuário já existe.")
        return

    if len(senha) < 4:
        print("Senha muito curta (mínimo 4 caracteres).")
        return

    salvar_usuario(usuario, senha)
    print("Cadastro realizado com sucesso!")


def login():
    usuarios = carregar_usuarios()

    usuario = input("Usuário: ").strip()
    senha = input("Senha: ").strip()

    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login realizado com sucesso!")
    else:
        print("Usuário ou senha incorretos.")


def menu():
    while True:
        print("\n1 - Cadastrar")
        print("2 - Login")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            login()
        elif opcao == "3":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")


# Executar sistema
menu()