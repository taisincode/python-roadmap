import requests

cep = input('Digite o CEP: ')
if not cep:
    print("CEP não informado")
else:  
    url = f"https://viacep.com.br/ws/{cep}/json/"


    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        
        if 'erro' in dados:
            print('CEP não encontrado')
        else:
            print('Cidade: ', dados.get('localidade', 'Não informado'))
            print('Estado: ', dados.get('uf', 'Não informado'))
            print('Região: : ', dados.get('regiao', 'Não informado'))
            print('DDD: ', dados.get('ddd', 'Não informado'))
           
    else:
        print("Erro:", resposta.status_code)
