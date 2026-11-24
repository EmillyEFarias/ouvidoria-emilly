reclamacao = []

opcao = -1

print("------------------- BEM-VINDO AO SISTEMA DE OUVIDORIA -------------------")

while opcao != 7:

    print("-------------------------- MENU PRINCIPAL -------------------------------")
    print("\n1) Listar Reclamações \n2) Adicionar Reclamação \n3) Pesquisar Reclamação \n4) Remover Reclamação \n5) Quantidade de Reclamações \n6) Substituir Reclamação \n7) Sair do Programa")

    print("-------------------------------------------------------------------------")

    opcao = int(input("Digite uma opção de 1 a 7: "))

    print("A opção lida foi", opcao)

    if opcao == 1:

        if len(reclamacao) > 0:
            print("Lista de Reclamações:")

            for item in range(len(reclamacao)):
                print(item +1, "-", reclamacao[item])

        else:
            print("Nenhuma reclamação cadastrada!")

    elif opcao == 2:

        nova_reclamacao = input("Descreva sua reclamação: ")
        reclamacao.append(nova_reclamacao)

        print("Reclamação cadastrada com sucesso!")

    elif opcao == 3:

        busca = input("Digite uma palavra/expressão para consulta: ").lower()

        if len(reclamacao) > 0:
            for item in range(len(reclamacao)):
                if busca in reclamacao[item].lower():
                    print(item + 1, "-", reclamacao[item])

            else:
                print("Palavra/expressão não encontrada!")

        else:
            print("Nenhuma reclamação cadastrada!")

    elif opcao == 4:

        if len(reclamacao) > 0:
            print("Lista de Reclamações:")

            for item in range(len(reclamacao)):
                print(item +1, "-", reclamacao[item])

            codigo = int(input("Digite o código da reclamação a ser removida: "))

            if codigo > 0 and codigo <= len(reclamacao):
                reclamacao.pop(codigo - 1)
                print("Reclamação removida com sucesso!")

            else:
                print("O código informado é inválido!")

        else:
            print("Nenhuma reclamação cadastrada!")

    elif opcao == 5:

        print("Atualmente tem(os)", len(reclamacao), "reclamação(ões) cadastrada(s)!")

    elif opcao == 6:

        if len(reclamacao) > 0:
            print("Lista de Reclamações:")

            for item in range(len(reclamacao)):
                print(item + 1, "-", reclamacao[item])

            codigo = int(input("Digite o código da reclamação a ser substituída: "))

            if codigo > 0 and codigo <= len(reclamacao):
                nova_reclamacao = input("Descreva a nova reclamação: ")
                reclamacao[codigo - 1] = nova_reclamacao

                print("A reclamação foi substituída com sucesso!")

            else:
                print("O código informado é inválido!")

        else:
            print("Nenhuma reclamação cadastrada!")

    elif opcao == 7:

        print("Obrigado por utilizar o programa!")

    else:

        print("Opção inválida!")










