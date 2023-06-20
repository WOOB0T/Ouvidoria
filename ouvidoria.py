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

    elif escolha == 2:
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

    elif escolha == 3:
        print("\n" + "◆ Categorias de Manifestações:" + "\n")
        print("[ 1 ] Reclamações")
        print("[ 2 ] Sugestões")
        print("[ 3 ] Elogios")

        type = int(input("\n" + "▶ Digite pelo código em qual categoria você deseja cadastrar sua manifestação: "))

        if 0 < type < 4:
            title = input("\n" + "▶ Escreva um título que resuma sua manifestação:  ")
            description = input("▶ Por favor, descreva sua manifestação: ")
            nome = input("▶ Por fim, informe seu nome completo: ")

            sqlInsercao = 'insert into ocorrencias (tipo, titulo , descricao , autor) values (%s,%s,%s,%s)'
            valores = [str(type), title, description, nome]

            insertNoBancoDados(conexao, sqlInsercao, valores)
            print("\n" + "✔  Sua manifestação foi cadastrada com sucesso!")

        else:
            print("\n" + error.center(55, " "))

        print("\n" + redirect.center(55, " "))

    elif escolha == 4:
        ConsultaQuantidadeTotal = "select count(*) from ocorrencias"
        resultadoTotal = listarBancoDados(conexao, ConsultaQuantidadeTotal)

        consultaQuantidadeRec = "select count(*) from ocorrencias where tipo = 1"
        resultadoRec = listarBancoDados(conexao, consultaQuantidadeRec)

        consultaQuantidadeSug = "select count(*) from ocorrencias where tipo = 2"
        resultadoSug = listarBancoDados(conexao, consultaQuantidadeSug)

        consultaQuantidadeElo = "select count(*) from ocorrencias where tipo = 3"
        resultadoElo = listarBancoDados(conexao, consultaQuantidadeElo)

        print("\n" + "◆ No total, existem", resultadoTotal[0][0], "manifestações cadastradas. Dentre essas:")
        print("➥", resultadoRec[0][0], "são reclamações")
        print("➥", resultadoSug[0][0], "são sugestões")
        print("➥", resultadoElo[0][0], "são elogios")

    elif escolha == 5:
        codigo = int(input("\n" + "▶ Digite o protocolo da manifestação que deseja encontrar: "))

        consultaProtocol = 'select * from ocorrencias where protocolo = ' + str(codigo)
        ocorrenciaPesquisada = listarBancoDados(conexao, consultaProtocol)

        if len(ocorrenciaPesquisada) == 1:
            print("\n" + "⌕ A manifestação pesquisada foi:")
            for items in ocorrenciaPesquisada:
                print("\n" + "Categoria:", items[1], "\n" + "➥ Título:", items[2],
                      "\n" + "➥ Descrição:", items[3], "\n" + "➥ Autor:", items[4])

        else:
            print("\n" + error.center(55, " "))

    elif escolha == 6:

    if len(ocorrencias) == 0:
        print("\n" + "◆ Ainda não existem manifestações que possam ser alteradas!")

    else:
        codigo = input("\n" + "▶ Digite o protocolo da manifestação que deseja alterar: ")
        consultaAlt = "select * from ocorrencias where protocolo = " + codigo
        ocorrencia = listarBancoDados(conexao, consultaAlt)

        if len(ocorrencia) == 1:
            print("\n" + "⌕ A manifestação selecionada foi:")
            for items in ocorrencia:
                print("\n" + "Categoria:", items[1], "\n" + "➥ Título:", items[2],
                      "\n" + "➥ Descrição:", items[3], "\n" + "➥ Autor:", items[4])

            print("\n" + "◆ A seguir, você poderá modifica-la:")
            newTitle = input("\n" + "▶ Reescreva o título da manifestação: ")
            newDescription = input("▶ Adicione a nova descrição dessa manifestação: ")

            sqlAtualizar = "update ocorrencias set titulo = %s, descricao = %s  where protocolo = " + codigo
            valores = (newTitle, newDescription)
            atualizarBancoDados(conexao, sqlAtualizar, valores)

            print("\n" + "✓  A manifestação foi atualizada com sucesso!")

        else:
            print("\n" + error.center(55, " "))

        print("\n" + redirect.center(55, " ")

    elif escolha == 7:
        consultaOcorrencias = "select * from ocorrencias"
        ocorrencias = listarBancoDados(conexao, consultaOcorrencias)
        
        if len(ocorrencias) == 0:
            print("\n" + "◆ Ainda não existem manifestações que possam ser deletadas!")

        else:
            print("\n" + "◆ Opções disponiveis:" + "\n")
            print("[ 1 ] Remover Todas as Manifestações")
            print("[ 2 ] Remover Todas as Manifestações de uma Categoria")
            print("[ 3 ] Remover Manifestações Específicas")

            remove = int(input("\n" + "▶ Digite a opção que deseja realizar: "))

            if remove == 1:
                sqlDelet = "delete from ocorrencias"
                delAllBancoDados(conexao, sqlDelet)

                print("\n" + "✔  Todas as ocorrências foram removidas com sucesso!")

            elif remove == 2:
                print("\n" + "◆ Categorias de Manifestações:" + "\n")
                print("[ 1 ] Reclamações")
                print("[ 2 ] Sugestões")
                print("[ 3 ] Elogios")

                codigo = int(input("\n" + "▶ Digite o código da categoria que você deseja realizar a remoção: "))

                sqlDelet = "delete ocorrencias where tipo = %s "
                dados = (str(codigo),)
                excluirBancoDados(conexao, sqlDelet, dados)

                print("\n" + "✔  Todas as manifestações da categoria selecionada foram removidas com sucesso!")

            elif remove == 3:
                print("\n" + "◆ Manifestações cadastradas:")
                for items in ocorrencias:
                    print("\n" + "Protocolo:", items[0], "-", "Categoria:", items[1], "\n" + "➥ Título:", items[2])

                codigo = input("\n" + "▶ Digite o protocolo da manifestação que você deseja deletar: ")

                consultaProtocol = 'select * from ocorrencias where protocolo = ' + str(codigo)
                ocorrenciaPesquisada = listarBancoDados(conexao, consultaProtocol)

                if len(ocorrenciaPesquisada) == 1:
                    sqlDelet = "delete from ocorrencias where protocolo = %s "
                    dados = (codigo,)
                    excluirBancoDados(conexao, sqlDelet, dados)

                    print("\n" + "✔  A ocorrencia de protocolo", codigo, "foi removida com sucesso!")

                else:
                    print("\n" + error.center(55, " "))
            else:
                print("\n" + error.center(55, " "))

        print("\n" + redirect.center(55, " "))

    elif escolha == 8:
        print("\n" + "Agradecemos por ter utilizado o nosso sistema da Ouvidoria, "
                     "a opinião dos nossos associados é muito importante para nós!")

    else:
        print("\n" + error.center(55, " "))
        print("\n" + redirect.center(55, " "))

encerrarBancoDados(conexao)
