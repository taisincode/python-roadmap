from utils.validacao import validar_nome


def cadastrar_usuario(nome):
    if not validar_nome(nome):
        return "Nome inválido!"

    # Simulação de cadastro
    return f"Usuário '{nome}' cadastrado com sucesso!"