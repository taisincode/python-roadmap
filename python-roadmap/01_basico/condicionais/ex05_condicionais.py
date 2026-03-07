# 5 - Crie um sistema simples que peça login e senha e valide.

login_correto = "TaisPrates"
senha_correta = "54321"

login = input('login: ')
senha = input('senha: ')

if login == login_correto and senha == senha_correta:
    print('Login realizado com sucesso')
else:
    print("Usuário ou senha incorretos")