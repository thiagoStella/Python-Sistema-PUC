'''
Aluno: Thiago Stella Pontes
Curso: Análise e Desenvolvimento de Sistemas
'''
import json

def show_main_menu(): #função que mostra o menu principal
    print("****************************************")
    print("*****  Bem-Vindo ao Sistema PUC  *******")
    print("*****  ------------------------  *******")
    print("****************************************")
    print('MENU PRINCIPAL: ')
    print('1 - Estudantes')
    print('2 - Disciplinas')
    print('3 - Professores')
    print('4 - Turmas')
    print('5 - Matriculas')
    print('0 - Sair\n')
    # Opção do usuário no menu principal
    return input('Digite a opção desejada: ')

def show_sub_menu(): # função que mostra o menu de CRUD
    print('\n===== Menu de Operações =====')
    #CRUD Estudates
    print('1 - Incluir')
    print('2 - Listar')
    print('3 - Atualizar')
    print('4 - Excluir')
    print('5 - Voltar ao menu principal')
    print('\n')
    return input('Escolha a operação: ')

def create_record(nome_arquivo): #adiciona os valores 'matricula', 'nome' e 'cpf' as respectivas chaves
    estudante = {}
    estudante['matricula'] = input('\nDigite a matrícula: ')
    estudante['nome'] = input('Digite o nome do estudante: ')
    estudante['cpf'] = input('Digite o CPF: ')
    lista = ler_arquivo('estudantes.json')
    if lista is None:
        lista = []
    lista.append(estudante) #adiciona os dicionarios à lista 'estudantes'
    salvar_arquivo(lista, nome_arquivo)
    print('=================================')
    print('Estudante cadastrado com sucesso!\n\n')

def read_record(nome_arquivo): #verifica se a lista está vazia ou imprime a lista na tela 
    estudantes = ler_arquivo(nome_arquivo)
    if estudantes == []:
        print('Não há estudantes cadastrados')
    else:
        for estudante in estudantes:
            print(f'Dados do estudante: {estudante}')



def update_record(codigo, nome_arquivo): #verifica se o input consta na lista de estudantes, caso esteja abre a edição, caso não, retorna um msg.
    lista = ler_arquivo(nome_arquivo)
    codigo = input('Qual é o número da matrícula para atualizar? ')
    for aluno in lista:
        if aluno['matricula'] == codigo:
            aluno['matricula'] = input("Digite a nova matrícula: ")
            aluno['nome'] = input("Digite o novo nome: ")
            aluno['cpf'] = input("Digite o novo cpf: ")
            salvar_arquivo(lista, nome_arquivo)
            print('\nEstudante atualizado com sucesso!')
            return
    print('Códuigo não encontrado.')
            


def delete_record(codigo, nome_arquivo): #verifica se o input consta na lista, caso esteja ele exclui o estudante, caso não, retorna uma msg.
    excluir = input('Qual é o número da matrícula para excluir? ')
    removido = False
    lista = ler_arquivo(nome_arquivo)
    for aluno in lista:
        if aluno['matricula'] == excluir:
            removido = True
            lista.remove(aluno)
            salvar_arquivo(lista, 'estudantes.json')
            print('\nEstudante excluído com sucesso!')
    if not removido:
        print(f'Código {excluir} não encontrado')        

def salvar_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(lista, arquivo)

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            lista = json.load(arquivo)
        return lista
    except:
        return []

def processar_menu_secundario(opcao_secundaria, nome_arquivo):
    if opcao_secundaria == '1': 
        create_record(nome_arquivo)
    elif opcao_secundaria =='2': 
        read_record(nome_arquivo)
    elif opcao_secundaria =='3':
        update_record(opcao_secundaria, nome_arquivo)
    elif opcao_secundaria =='4':
        delete_record(opcao_secundaria, nome_arquivo)
    elif opcao_secundaria =='5': #encerra o menu de estudantes e volta ao principal
        return False
    else:
        print('Opção inválida')
    return True

arquivo_estudante = 'estudantes.json'
arquivo_disciplina = 'disciplinas.json'

while True:
    opcao = show_main_menu()
    
    if opcao == '1': #direciona para o menu de estudantes
        while True:
            opcao_secundaria = show_sub_menu()
            if not processar_menu_secundario(opcao_secundaria, arquivo_estudante):
                break

    elif opcao == '2':
        while True:
            opcao_secundaria = show_sub_menu()
            if not processar_menu_secundario(opcao, arquivo_disciplina):
                break
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