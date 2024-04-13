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
            if opcao_estudantes == '1': #adiciona os valores 'matricula', 'nome' e 'cpf' as respectivas chaves
                aluno = {}
                aluno['matricula'] = int(input('Digite a matrícula: '))
                aluno['nome'] = input('Digite o nome do estudante: ')
                aluno['cpf'] = input('Digite o CPF: ')
                estudantes.append(aluno) #adiciona os dicionarios à lista 'estudantes'
                print('=================================')
                print('Estudante cadastrado com sucesso!\n\n')
            elif opcao_estudantes =='2': #verifica se a lista está vazia ou imprime a lista na tela 
                if estudantes == []:
                    print('Não há estudantes cadastrados')
                else:
                    for i in estudantes:
                        print(i)
            elif opcao_estudantes =='3':
                editar = int(input('Qual é o número da matrícula para atualizar? '))
                editado = None
                for aluno in estudantes:
                    if aluno['matricula'] == editar:
                        editado = aluno
                        break
                if editado is None:
                    print(f'Código {excluir} não encontrado')
                else:
                    editado['matricula'] = int(input("Digite a nova matrícula: "))
                    editado['nome'] = input("Digite o novo nome: ")
                    editado['cpf'] = input("Digite o novo cpf: ")
                    
                print('Estudante atualizado com sucesso!')
            elif opcao_estudantes =='4':
                excluir = int(input('Qual é o número da matrícula para excluir? '))
                removido = None
                for aluno in estudantes:
                    if aluno['matricula'] == excluir:
                        removido = aluno
                        break
                if removido is None:
                    print(f'Código {excluir} não encontrado')
                else:
                    estudantes.remove(removido)
                print(f'Estudante {aluno['nome']} foi excluido com sucesso!')
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