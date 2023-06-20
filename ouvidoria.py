# Integrantes do Grupo:

# Jessica Vitória Luiz Batista
# Renata Cardoso Mantovani
# Fábio José Dantas Filho
# Thayse Fernanda Silva de Barros
# Evelyn Julia da Silva
# Tiago Sousa Gomes

# comandos importados:
from main import *
from time import sleep

# variáveis de mensagens automáticas:
loading = "↻ Carregando..."
acesso = "Acesso liberado por Jack! 🐊"
redirect = "Iremos lhe redirecionar para o menu principal."
error = "⚠︎ A opção inserida é inválida! ⚠︎"

# Banco de Dados:
conexao = abrirBancoDados('localhost', 'root', '12345', 'ouvidoria')

# MENU:
escolha = 333
while escolha != 8:

    print("\n" + loading.center(55, " ") + "\n")
    sleep(2.5)

    print("       ┏━━━━━━━━━━━━━┓")
    print("             MENU     ")
    print("       ┗━━━━━━━━━━━━━┛" + "\n")
    print("[ 1 ] Listar Manifestações")
    print("[ 2 ] Listar Manifestações por Categoria")
    print("[ 3 ] Cadastrar Manifestações")
    print("[ 4 ] Exibir Quantidade de Manifestações")
    print("[ 5 ] Consultar Manifestações por Código")
    print("[ 6 ] Alterar Manifestações")
    print("[ 7 ] Deletar Manifestações")
    print("[ 8 ] Sair da Ouvidoria" + "\n")

    escolha = int(input("▶ Escolha a opção que deseja acessar: "))

    if escolha == 1:
        consultaOcorrencias = "select * from ocorrencias"
        ocorrencias = listarBancoDados(conexao, consultaOcorrencias)

        if len(ocorrencias) == 0:
            print("\n" + "◆ Ainda não existem manifestações a serem exibidas!")

        else:
            print("\n" + "◆ Manifestações cadastradas até o momento:")

            for items in ocorrencias:
                print("\n" + "Protocolo:", items[0], "-", "Categoria:", items[1], "\n" + "➥ Título:", items[2],
                  "\n" + "➥ Descrição:", items[3], "\n" + "➥ Autor:", items[4])

            print("\n" + "◆ Fim da listagem.")

        print("\n" + redirect.center(55, " "))

    if escolha == 2:
        print()
        print("-", "Lista: Categorias de Manifestações", "-")
        print("[1] Reclamações")
        print("[2] Sugestões")
        print("[3] Elogios")
        print()

        categoria = int(input("▶ Digite a categoria da manifestação que deseja listar:"))

        if 0 < categoria < 4:

            listagemTipo = "select * from ocorrencias where tipo =" + str(categoria)
            ocorrenciasTipo = listarBancoDados(conexao, listagemTipo)

            if len(ocorrenciasTipo) == 0:
                print("Ainda não existem manifestações nessa categoria!")

            else:
                print('-', "Manifestações cadastradas até o momento:")
                for o in ocorrenciasTipo:
                    print("Protocolo: ", o[0], "/", "Título:", o[2], "/", "Autor:", o[4])

                print("\n" + "◆ Fim da listagem.")

        else:
            print("\n" + error.center(55, " "))

        print("\n" + redirect.center(55, " "))