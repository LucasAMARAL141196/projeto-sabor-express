import os # Biblioteca para limpar a tela do terminal

restaurantes = ['Pizza', 'Sushi']  # Lista de restaurantes cadastrados

def exibir_nome_do_programa(): # Função para exibir o nome do programa
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opcoes(): # Função para exibir as opções do menu
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app(): # Função para finalizar o aplicativo
    exibir_subtitulo('Finalizar app')

def voltar_ao_menu_principal(): # Função para voltar ao menu principal
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida(): # Função para exibir mensagem de opção inválida
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto): # Função para exibir um subtítulo e limpar a tela
    os.system('cls') # Limpa a tela do terminal
    print(texto)
    print()

def cadastrar_novo_restaurante(): # Função para cadastrar um novo restaurante
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante) # Adiciona o nome do restaurante à lista de restaurantes cadastrados
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_ao_menu_principal()

def listar_restaurantes(): # Função para listar os restaurantes cadastrados
    exibir_subtitulo('Listando restaurantes')

    for restaurante in restaurantes: # Percorre a lista de restaurantes cadastrados e exibe cada um deles
        print(f'.{restaurante}')

    voltar_ao_menu_principal()

def escolher_opcao(): # Função para escolher uma opção do menu
    try:# Bloco try para capturar erros de entrada do usuário
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            print('Ativar restaurante')
        elif opcao_escolhida == 4: 
            finalizar_app()
        else: 
            opcao_invalida()
    except: # Se ocorrer um erro de entrada do usuário, exibe a mensagem de opção inválida
        opcao_invalida()

def main(): # Função principal do aplicativo
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__': # Verifica se o script está sendo executado diretamente (e não importado como módulo) e chama a função main()
    main()