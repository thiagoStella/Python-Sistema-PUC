print("****************************************")
print("*****  Bem-Vindo ao Sistema PUC  *******")
print("****************************************")

# mostrar menu
print("Menu principal: (navegação pelo índice)")
print("1 - Estudantes")
print("2 - Disciplinas")
print("3 - Professores")
print("4 - Turmas")
print("5 - Matriculas")
print("0 - Sair")
print("  ")

# Opção do usuário
opcao = input("Digite a opção desejada: ")
if opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4" or opcao == "5":
    print("  ")
    print("-----> Você escolheu a opção ", opcao , "...")
    print("  ")
    # menu CRUD

    print("Menu: Categoria ", opcao , " (navegação pelo índice):")
    print("1 - Incluir")
    print("2 - Listar")
    print("3 - Atualizar")
    print("4 - Excluir")
    print("5 - Voltar ao menu principal")
    print("  ")

    opcao_menu = input("Digite a opção desejada: ")
    if opcao_menu == "1" or opcao_menu == "2" or opcao_menu == "3" or opcao_menu == "4" or opcao_menu == "5":
        print("  ")
        print("-----> Você escolheu a opção ", opcao_menu )
        print("  ")
    else:
        print("  ")
        print("Opção I-N-V-Á-L-I-D-A")
        print("  ")
elif opcao == "0":
    print("SAINDO DO SISTEMA")

else:
    print("  ")
    print("Opção I-N-V-Á-L-I-D-A")
    print("  ")

    
