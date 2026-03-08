# Dicionário armazena dados em formato chave: valor.
personagem_principal = {
    'nome':'Evie Blake',
    'idade':19,
    'curso':'Relações Internacionais'
}

print(personagem_principal['nome']) 
print(personagem_principal.get('altura')) #usar .get é mais seguro. Caso a chave não exixtir ele vai retornar None ou pode definir um valor padrão como "Não informado".

print(personagem_principal.get("altura","Não informado")) #retorna "Não informado".
print(personagem_principal.get("nome","Não informado")) #retorna nome normalmente

print(personagem_principal.keys()) #retorna o nome das chaves: dict_keys(['nome', 'idade', 'curso'])

print(personagem_principal.values()) #retorna todos os valores: dict_values(['Evie Blake', 19, 'Relações Internacionais'])

print(personagem_principal.items()) #retorna as chaves e seus valores: dict_items([('nome', 'Evie Blake'), ('idade', 19), ('curso', 'Relações Internacionais')])

for chave,valor in personagem_principal.items():
    print(chave, valor) #retorna chave e valor em ordem crescente: nome Evie Blake, idade 19, curso Relações Internacionais
    
personagem_principal.update({'altura':1.68}) #adiciona chave
personagem_principal.update({'nome':'Evie B.'}) #atualiza chave

for chave,valor in personagem_principal.items():
    print(chave, valor) #retorna chave e valor em ordem crescente: nome Evie Blake, idade 19, curso Relações Internacionais