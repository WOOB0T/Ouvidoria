def consultarPeloCodigo(conexao):
    codigo = input(
        "\n" + "▶ Digite o protocolo da manifestação que deseja encontrar: "
    )
    consultaProtocol = "select * from manifestaçao where codigo =" + str(codigo)
    ocorrenciaPesquisada = listarBancoDados(conexao, consultaProtocol)

    if len(ocorrenciaPesquisada) == 1:
        print("\n" + "⌕ A manifestação pesquisada foi:")
        for items in ocorrenciaPesquisada:
            print(
                "\n" + "➥ Categoria:",
                items[1],
                "\n" + "➥ Título:",
                items[2],
                "\n" + "➥ Descrição:",
                items[3],
                "\n" + "➥ Autor:",
                items[4],
            )

    else:
        print("\n" + "◆ Não existe nenhuma manifestação com esse protocolo!")
