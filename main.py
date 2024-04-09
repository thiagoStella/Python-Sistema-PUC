while True:
    print("                                        ")
    print("****************************************")
    print("*****  Bem-Vindo ao Sistema PUC  *******")
    print("*****  ------------------------  *******")
    print("****************************************")
    print("                                        ")

    # mostrar menu
    print('MENU PRINCIPAL: ')
    print('1 - Estudantes')
    print('2 - Disciplinas')
    print('3 - Professores')
    print('4 - Turmas')
    print('5 - Matriculas')
    print('0 - Sair')
    print(' ')

    # Opção do usuário
    opcao = input("Digite a opção desejada: ")
    if opcao == '1' or opcao == '2' or opcao == '3' or opcao == '4' or opcao == '5':
        while True:
            print(f'===== Menu {opcao} =====\n\n')

        # menu CRUD
            print("Menu cadastro (navegação pelo índice):")
            print("1 - Incluir")
            print("2 - Listar")
            print("3 - Atualizar")
            print("4 - Excluir")
            print("5 - Voltar ao menu principal")
            print("  ")
            opcao_secundaria = input("Digite a operação: ")

            if opcao_secundaria == '1' or opcao_secundaria == '2' or opcao_secundaria == '3' or opcao_secundaria == '4':
                print(f'===== Você escolheu a operação {opcao_secundaria} =====')
                print("  ")
                print("  ")
            elif opcao_secundaria =='5':
                break
            else:
                print('Opção inválida')
    elif opcao == '0':
        print("Fazendo o logoff do sistema...\n\n")
        break
    else:
        print("OPÇÃO INVÁLIDA!")