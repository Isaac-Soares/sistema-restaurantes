import os
import requests

restaurantes = [
    {
        "nome": "Praca",
        "categoria": "Japonesa",
        "cidade": "Brasília",
        "estado": "DF",
        "ativo": False
    },

    {
        "nome": "Pizza Suprema",
        "categoria": "Pizza",
        "cidade": "Goiânia",
        "estado": "GO",
        "ativo": True
    },

    {
        "nome": "Cantina",
        "categoria": "Italiano",
        "cidade": "São Paulo",
        "estado": "SP",
        "ativo": False
    }
]


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
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar estado do restaurante')
    print('4. Sair\n')


def finalizar_app():
    exibir_subtitulo('Finalizando app')


def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()


def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()


def exibir_subtitulo(texto):

    os.system('cls')

    linha = '*' * (len(texto) + 4)

    print(linha)
    print(texto)
    print(linha)
    print()


def cadastrar_novo_restaurante():

    exibir_subtitulo('Cadastro de novos restaurantes')

    nome_do_restaurante = input(
        'Digite o nome do restaurante que deseja cadastrar: '
    )

    categoria = input(
        f'Digite a categoria do restaurante {nome_do_restaurante}: '
    )

    cep = input('Digite o CEP do restaurante: ')

    url = f'https://viacep.com.br/ws/{cep}/json/'

    response = requests.get(url)

    dados = response.json()

    cidade = dados['localidade']
    estado = dados['uf']

    print(f'\nCidade encontrada: {cidade}')
    print(f'Estado encontrado: {estado}')

    dados_do_restaurante = {
        "nome": nome_do_restaurante,
        "categoria": categoria,
        "cidade": cidade,
        "estado": estado,
        "ativo": False
    }

    restaurantes.append(dados_do_restaurante)

    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!')

    voltar_ao_menu_principal()


def listar_restaurantes():

    exibir_subtitulo('Listando restaurantes')

    print(
        f'{"Nome".ljust(20)} | '
        f'{"Categoria".ljust(20)} | '
        f'{"Cidade".ljust(15)} | '
        f'{"Estado".ljust(10)} | '
        f'Status'
    )

    for restaurante in restaurantes:

        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        cidade = restaurante["cidade"]
        estado = restaurante["estado"]

        ativo = 'ativado' if restaurante["ativo"] else 'desativado'

        print(
            f'{nome_restaurante.ljust(20)} | '
            f'{categoria.ljust(20)} | '
            f'{cidade.ljust(15)} | '
            f'{estado.ljust(10)} | '
            f'{ativo}'
        )

    voltar_ao_menu_principal()


def alternar_estado_restaurante():

    exibir_subtitulo('Alterando estado do restaurante')

    nome_restaurante = input(
        'Digite o nome do restaurante que deseja alterar o estado: '
    )

    restaurante_encontrado = False

    for restaurante in restaurantes:

        if nome_restaurante == restaurante["nome"]:

            restaurante_encontrado = True

            restaurante["ativo"] = not restaurante["ativo"]

            mensagem = (
                f'O restaurante {nome_restaurante} foi ativado com sucesso'
                if restaurante["ativo"]
                else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            )

            print(mensagem)

    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')

    voltar_ao_menu_principal()


def escolher_opcao():

    try:

        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            alternar_estado_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()

    except:
        opcao_invalida()


def main():

    os.system('cls')

    exibir_nome_do_programa()

    exibir_opcoes()

    escolher_opcao()


if __name__ == '__main__':
    main()