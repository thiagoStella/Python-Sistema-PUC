'''
Aluno: Thiago Stella Pontes
Curso: Análise e Desenvolvimento de Sistemas
'''

#bloco de listas de operações
estudantes = []


while True: #persistência no menu enquanto não entra na linha 67
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
    print('\n\n')
    # Opção do usuário no menu principal
    opcao = input('Digite a opção desejada: \n\n')
    
    if opcao == '1': #direciona para o menu de estudantes
        while True:
            print('\n\n===== Menu [ESTUDANTES] =====\n')
            #CRUD Estudates
            print('Menu cadastro:')
            print('1 - Incluir')
            print('2 - Listar')
            print('3 - Atualizar')
            print('4 - Excluir')
            print('5 - Voltar ao menu principal')
            print('\n')
            opcao_estudantes = input('Escolha a operação: ')
            if opcao_estudantes == '1': #adiciona o nome na variável aluno e depois faz um append na lista de estudantes
                aluno = input('Digite o nome do aluno: ')
                estudantes.append(aluno)
            elif opcao_estudantes =='2': #verifica se a lista está vazia ou imprime a lista formatada na tela 
                if estudantes == []:
                    print('Não há estudantes cadastrados')
                else:
                    for i in range(len(estudantes)):
                        print("-",estudantes[i])
            elif opcao_estudantes =='3':
                print('\n\nEM DESENVOLVIMENTO')
            elif opcao_estudantes =='4':
                print('\n\nEM DESENVOLVIMENTO')
            elif opcao_estudantes =='5': #encerra o menu de estudantes e volta ao principal
                break
            else:
                print('Opção inválida')
    elif opcao == '2':
        print('\n\nEM DESENVOLVIMENTO')
    elif opcao == '3':
        print('\n\nEM DESENVOLVIMENTO')
    elif opcao == '4':
        print('\n\nEM DESENVOLVIMENTO')
    elif opcao == '5':
        print('\n\nEM DESENVOLVIMENTO')
    elif opcao == '0': #encerra a aplicação
        print("\n\nFazendo o logoff do sistema...\n\n")
        break
    else:
        print("\n\nOPÇÃO INVÁLIDA!")