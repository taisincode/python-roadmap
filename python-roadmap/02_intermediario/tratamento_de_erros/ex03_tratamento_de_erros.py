#Ex03 = sistema simples que:
#- Tente abrir um arquivo chamado `dados.txt`
#- Se não existir, mostre uma mensagem amigável


try:
    with open('dados.txt', 'r') as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("Arquivo 'dados.txt' não encontrado.")