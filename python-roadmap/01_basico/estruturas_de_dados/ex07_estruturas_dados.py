#7- Mostre os valores de um dicionário usando loop.

personagem_principal = {
    'nome': 'Evie Blake',
    'idade': 19,
    'curso': 'Relações Internacionais'
}

# inicia um loop for para percorrer os valores do dicionário
# personagem_principal.values() pega somente os valores
# ou seja: 'Evie Blake', 19 e 'Relações Internacionais'
for valor in personagem_principal.values():
    
    # mostra cada valor na tela, um por vez
    print(valor)