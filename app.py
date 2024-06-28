import os

restaurantes = []

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
      """)

def exibir_opcoes():
    print('1. Cadastrar restaurante','2. Listar restaurantes','3. Ativar restaurante','4. Sair\n', sep = '\n')

def opcao_invalida():
    print('Opção inválida!')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def cadastrar_novo_restaurante():
    os.system('cls')
    print('Cadastrar novo restaurante\n')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_do_restaurante)
    print(f'o restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    input('Digite uma tecla para voltar ao menu principal: ')
    main()

def escolher_opcao():
    try:
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            cadastrar_novo_restaurante()
        elif opcao == 2:
            print('Listar restaurantes')
        elif opcao == 3:
            print('Ativar restaurante')
        elif opcao == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def finalizar_app():
    os.system('cls')
    print('Finalizando o app\n')

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()