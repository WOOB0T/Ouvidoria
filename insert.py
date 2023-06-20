elif escolha == 3:\
    print("\n" + "◆ Categorias de Manifestações:" + "\n")
    print("[ 1 ] Reclamações")
    print("[ 2 ] Sugestões")
    print("[ 3 ] Elogios")

type = int(input("\n" + "▶ Digite pelo código em qual categoria você deseja cadastrar sua manifestação: "))

if 0 < type < 4:
    title = input("\n" + "▶ Escreva um título que resuma sua manifestação:  ")
    description = input("▶ Por favor, descreva sua manifestação: ")

    sqlInsercao = 'insert into ocorrencias (tipo, titulo , descricao , autor) values (%s,%s,%s,%s)'
    valores = [str(type), title, description, nome]

    insertNoBancoDados(conexao, sqlInsercao, valores)
    print("\n" + "✔  Sua manifestação foi cadastrada com sucesso!")

else:
    print("\n" + error.center(55, " "))

    print("\n" + redirect.center(55, " "))