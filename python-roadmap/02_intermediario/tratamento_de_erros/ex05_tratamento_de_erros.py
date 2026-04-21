while True:
    print("\n1 - Somar")
    print("2 - Dividir")
    print("3 - Sair")

    try:
        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            try:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print("Resultado:", a + b)
            except ValueError:
                print("Entrada inválida.")

        elif opcao == 2:
            try:
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
                print("Resultado:", a / b)
            except ValueError:
                print("Entrada inválida.")
            except ZeroDivisionError:
                print("Erro: divisão por zero.")

        elif opcao == 3:
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida.")

    except ValueError:
        print("Digite um número válido para a opção.")