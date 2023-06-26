# 2 - LISTAR POR CATEGORIA (MENU)
def listarPorCategoria(conexao):
    categoriasOcorrencias()
    categoria = int(input("▶ Digite a categoria de manifestação que você deseja listar: "))

    if 0 < categoria < 4:
        ocorrenciasTipo = listarFromColumn(conexao, "tipo", str(categoria))

        if len(ocorrenciasTipo) == 0:
            print("\n" + "◆ Ainda não existem manifestações a serem exibidas nessa categoria!")

        else:
            print("\n" + "◆ Manifestações cadastradas na categoria até o momento:")
            for items in ocorrenciasTipo:
                sleep(1.75)
                print("\n" + "Protocolo:", items[0], "\n" + "➥ Título:", items[2], "\n" + "➥ Descrição:",
                      items[3], "\n" +
                      "➥ Autor:", items[4])
                sleep(1.75)

            print("\n" + "◆ Fim da listagem.")

    else:
        print("\n" + error.center(55, " "))