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
    aluno['matricula'] = input('\nDigite a matrícula: ')
    aluno['nome'] = input('Digite o nome do estudante: ')
    aluno['cpf'] = input('Digite o CPF: ')
    estudantes.append(aluno) #adiciona os dicionarios à lista 'estudantes'
    print('=================================')
    print('Estudante cadastrado com sucesso!\n\n')

def read_student(): #verifica se a lista está vazia ou imprime a lista na tela 
    if estudantes == []:
        print('Não há estudantes cadastrados')
    else:
        for aluno in estudantes:
            for chave, valor in aluno.items():
                print(f'{chave}: {valor}', end=' | ')
            print()



def update_student(): #verifica se o input consta na lista de estudantes, caso esteja abre a edição, caso não, retorna um msg.
    editar = input('Qual é o número da matrícula para atualizar? ')
    editado = False
    for aluno in estudantes:
        if aluno['matricula'] == editar:
            editado = True            
            aluno['matricula'] = input("Digite a nova matrícula: ")
            aluno['nome'] = input("Digite o novo nome: ")
            aluno['cpf'] = input("Digite o novo cpf: ")
            print('\nEstudante atualizado com sucesso!')
    if not editado:
        print(f'Matricula {editar} não encontrada')
            


def delete_student(): #verifica se o input consta na lista, caso esteja ele exclui o estudante, caso não, retorna uma msg.
    excluir = input('Qual é o número da matrícula para excluir? ')
    removido = False
    for aluno in estudantes:
        if aluno['matricula'] == excluir:
            removido = True
            estudantes.remove(aluno)
            print('\nEstudante excluído com sucesso!')
    if not removido:
        print(f'Código {excluir} não encontrado')        

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