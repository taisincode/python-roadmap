# ==========================================
# EXERCÍCIO: Crie um menu com 3 opções que repete até escolher sair.
# ==========================================


# -------------------------------
# Minha solução
# -------------------------------


print('\n Saída permitida somente se acertar minha cor favorita.')

while True:
    print('\n1 - Azul')
    print('2 - Lilás')
    print('3 - Rosa')

    opcao = input("Escolha: ")

    if opcao == "1":
        print('\n Gosto de azul, mas não é a minha cor favorita.')
    elif opcao == "2":
        print('\n Acertou! Atualmente lilás é minha cor favorita')
        break
    elif opcao == "3":
        print('\n Está próximo .')
    else:
        print("Opção inválida")