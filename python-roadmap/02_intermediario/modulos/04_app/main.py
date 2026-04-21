from usuarios.cadastro import cadastrar_usuario

nome = input("Digite o nome do usuário: ")
resultado = cadastrar_usuario(nome)

print(resultado)