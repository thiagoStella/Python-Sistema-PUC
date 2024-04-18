'''
Aluno: Thiago Stella Pontes
Curso: Análise e Desenvolvimento de Sistemas
'''
estudantes = []

def show_main_menu(): #função que mostra o menu principal
    print("                                        ")
    print("****************************************")
    print("*****  Bem-Vindo ao Sistema PUC  *******")
    print("*****  ------------------------  *******")
    print("****************************************")
    print("                                        ")

    print('MENU PRINCIPAL: ')
    print('1 - Estudantes')
    print('2 - Disciplinas')
    print('3 - Professores')
    print('4 - Turmas')
    print('5 - Matriculas')
    print('0 - Sair\n')
    # Opção do usuário no menu principal
    return input('Digite a opção desejada: ')

def show_student_menu():
    print('\n\n===== Menu [ESTUDANTES] =====')
    #CRUD Estudates
    print('Menu de cadastro:')
    print('1 - Incluir')
    print('2 - Listar')
    print('3 - Atualizar')
    print('4 - Excluir')
    print('5 - Voltar ao menu principal')
    print('\n')
    return input('Escolha a operação: ')

def create_student(): #adiciona os valores 'matricula', 'nome' e 'cpf' as respectivas chaves
    aluno = {}
    aluno['matricula'] = int(input('\nDigite a matrícula: '))
    aluno['nome'] = input('Digite o nome do estudante: ')
    aluno['cpf'] = input('Digite o CPF: ')
    estudantes.append(aluno) #adiciona os dicionarios à lista 'estudantes'
    print('=================================')
    print('Estudante cadastrado com sucesso!\n\n')

def read_student(): #verifica se a lista está vazia ou imprime a lista na tela 
    if estudantes == []:
        print('Não há estudantes cadastrados')
    else:
        for i in estudantes:
            print(i)

def update_student():
    aluno = ''
    editar = int(input('Qual é o número da matrícula para atualizar? '))
    editado = None
    for aluno in estudantes:
        if aluno['matricula'] == editar:
            editado = aluno
        break
    if editado != None:
        editado['matricula'] = int(input("Digite a nova matrícula: "))
        editado['nome'] = input("Digite o novo nome: ")
        editado['cpf'] = input("Digite o novo cpf: ")
        print('\nEstudante atualizado com sucesso!')
        
    else:
        print(f'Código {editar} não encontrado')
            

def delete_student():
    aluno = ''
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

while True:
    opcao = show_main_menu()
    
    if opcao == '1': #direciona para o menu de estudantes
        while True:
            opcao_estudantes = show_student_menu()
            if opcao_estudantes == '1': 
                create_student()
            elif opcao_estudantes =='2': 
                read_student()
            elif opcao_estudantes =='3':
                update_student()
            elif opcao_estudantes =='4':
                delete_student()
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