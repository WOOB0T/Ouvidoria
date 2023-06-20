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
