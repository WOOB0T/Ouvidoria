elif escolha == 2:
    print()
    print("\n" + "◆ Categorias de Manifestações" + "\n")
    print("[1] Reclamações")
    print("[2] Sugestões")
    print("[3] Elogios")
    print()

    categoria = int(input("▶ Digite a categoria da manifestação que deseja listar:"))

    if 0 < categoria < 4:

        listagemTipo = "select * from ocorrencias where tipo =" + str(categoria)
        ocorrenciasTipo = listarBancoDados(conexao, listagemTipo)

        if len(ocorrenciasTipo) == 0:
            print("◆ Ainda não existem manifestações nessa categoria!")

        else:
            print("\n" + "◆ Manifestações cadastradas até o momento:")
            for o in ocorrenciasTipo:
                print("\n" + "➥ Protocolo: ", o[0], "\n" + "➥ Título:", o[2], "\n" + "➥ Autor:", o[4])

            print("\n" + "◆ Fim da listagem.")

    else:
        print("\n" + error.center(55, " "))

    print("\n" + redirect.center(55, " "))
