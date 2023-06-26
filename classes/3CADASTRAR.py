# 3 - CADASTRAR NA TABELA "OCORRENCIAS" (MENU)
def cadastrarOcorrencias(conexao, nome):
    categoriasOcorrencias()
    type = int(input("▶ Digite pelo código em qual categoria você deseja cadastrar sua manifestação: "))

    if 0 < type < 4:
        print("\n" + "◆ Opções de cadastro:" + "\n")
        print("[ 1 ] Sob seu nome")
        print("[ 2 ] Em Anonimato" + "\n")

        userCadastro = int(input("▶ Digite pelo código a forma na qual você deseja cadastrar sua manifestação: "))

        if userCadastro == 2:
            nome = "Anônimo"

        title = input("\n" + "▶ Escreva um título que resuma sua manifestação: ")
        description = input("▶ Por favor, descreva sua manifestação: ")

        sqlInsercao = 'insert into ocorrencias (tipo, titulo , descricao , autor) values (%s,%s,%s,%s)'
        valores = [str(type), title, description, nome]

        protocolo = insertNoBancoDados(conexao, sqlInsercao, valores)
        print("\n" + "✔  Sua manifestação foi cadastrada com sucesso! O número do seu protocolo é:",protocolo)

    else:
        print("\n" + error.center(55, " "))

# 3.1 - CADASTRAR NA TABELA DA CATEGORIA
def cadastrarOcorrenciasEmCategoria(conexao, categoria, id, title, description, name):

    if categoria == 1:

        tabela = "reclamacoes"

    elif categoria == 2:

        tabela = "sugestoes"

    else:
        tabela = "elogios"

    sqlInsercao = "insert into " + tabela + " (protocolo, titulo, descricao, autor) values (%s,%s,%s,%s)"
    valores = [id, title, description, name]

    insertNoBancoDados(conexao, sqlInsercao, valores)

# 3.2 - CADASTRAR NA TABELA DE USUARIOS
def cadastroUsuarios(conexao, setor):
    print("\n" + loading.center(55, " ") + "\n")
    sleep(2.5)

    if 0 < setor < 4:

        nome = input("▶ Digite o seu nome completo: ")
        email = input("▶ Nos informe seu e-mail institucional: ")
        nomeSplit = nome.split()

        if setor == 1:
            print("\n" + "◆ Olá, " + nomeSplit[0] + "! Precisamos que compartilhe conosco algumas informações institucionais." + "\n")
            curso = input("▶ Digite o curso você faz na universidade: ")
            matricula = input("▶ Por fim, digite o seu número de matrícula: ")

            sqlInsertAssociados = "insert into estudantes (matricula,nome,curso,email_inst) values (%s,%s,%s,%s)"
            valores = [matricula, nome, curso, email]

            insertAssociadosNoBancoDados(conexao, sqlInsertAssociados, valores)

        elif setor == 2:
            print("\n" + "◆ Olá, Prof. " + nomeSplit[1] + "! Precisamos que compartilhe conosco algumas informações institucionais." + "\n")

            curso = input("▶ Digite para qual curso você leciona: ")
            disciplina = input("▶ Digite quais disciplinas você leciona em " + curso + ": ")
            id = input("▶ Por fim, digite seu número de identificação: ")

            sqlInsertAssociados = "insert into docentes (id,nome,curso,disciplinas,email_inst) values (%s,%s,%s,%s,%s)"
            valores = [id, nome, curso, disciplina, email]

            insertAssociadosNoBancoDados(conexao, sqlInsertAssociados, valores)

        elif setor == 3:
            print("\n" + "◆ Olá, " + nomeSplit[0] + "! Precisamos que compartilhe conosco algumas informações institucionais." + "\n")
            departamento = input("▶ Digite o departamento da universidade no qual você trabalha: ")
            id = input("▶ Por fim, digite o seu número de identificação: ")

            sqlInsertAssociados = "insert into colaboradores (id,nome,depart,email_inst) values (%s,%s,%s,%s)"
            valores = [id, nome, departamento, email]

            insertAssociadosNoBancoDados(conexao, sqlInsertAssociados, valores)

    else:
        print(error + "\n" +
              "De antemão, deve ser alertado que essa Ouvidoria é um sistema direcionado somente à "
              "associados do centro universitário." + "\n" + "Se esse não for o seu caso, o acesso não será permitido.")

    return nome

# 3 - CADASTRAR NA TABELA "OCORRENCIAS" (MENU)
def cadastrarOcorrencias(conexao, nome):
    categoriasOcorrencias()
    type = int(input("▶ Digite pelo código em qual categoria você deseja cadastrar sua manifestação: "))

    if 0 < type < 4:
        print("\n" + "◆ Opções de cadastro:" + "\n")
        print("[ 1 ] Sob seu nome")
        print("[ 2 ] Em Anonimato" + "\n")

        userCadastro = int(input("▶ Digite pelo código a forma na qual você deseja cadastrar sua manifestação: "))

        if userCadastro == 2:
            nome = "Anônimo"

        title = input("\n" + "▶ Escreva um título que resuma sua manifestação: ")
        description = input("▶ Por favor, descreva sua manifestação: ")

        sqlInsercao = 'insert into ocorrencias (tipo, titulo , descricao , autor) values (%s,%s,%s,%s)'
        valores = [str(type), title, description, nome]

        protocolo = insertNoBancoDados(conexao, sqlInsercao, valores)
        print("\n" + "✔  Sua manifestação foi cadastrada com sucesso! O número do seu protocolo é:",protocolo)

    else:
        print("\n" + error.center(55, " "))

# 3.1 - CADASTRAR NA TABELA DA CATEGORIA
def cadastrarOcorrenciasEmCategoria(conexao, categoria, id, title, description, name):

    if categoria == 1:

        tabela = "reclamacoes"

    elif categoria == 2:

        tabela = "sugestoes"

    else:
        tabela = "elogios"

    sqlInsercao = "insert into " + tabela + " (protocolo, titulo, descricao, autor) values (%s,%s,%s,%s)"
    valores = [id, title, description, name]

    insertNoBancoDados(conexao, sqlInsercao, valores)

# 3.2 - CADASTRAR NA TABELA DE USUARIOS
def cadastroUsuarios(conexao, setor):
    print("\n" + loading.center(55, " ") + "\n")
    sleep(2.5)

    if 0 < setor < 4:

        nome = input("▶ Digite o seu nome completo: ")
        email = input("▶ Nos informe seu e-mail institucional: ")
        nomeSplit = nome.split()

        if setor == 1:
            print("\n" + "◆ Olá, " + nomeSplit[0] + "! Precisamos que compartilhe conosco algumas informações institucionais." + "\n")
            curso = input("▶ Digite o curso você faz na universidade: ")
            matricula = input("▶ Por fim, digite o seu número de matrícula: ")

            sqlInsertAssociados = "insert into estudantes (matricula,nome,curso,email_inst) values (%s,%s,%s,%s)"
            valores = [matricula, nome, curso, email]

            insertAssociadosNoBancoDados(conexao, sqlInsertAssociados, valores)

        elif setor == 2:
            print("\n" + "◆ Olá, Prof. " + nomeSplit[1] + "! Precisamos que compartilhe conosco algumas informações institucionais." + "\n")

            curso = input("▶ Digite para qual curso você leciona: ")
            disciplina = input("▶ Digite quais disciplinas você leciona em " + curso + ": ")
            id = input("▶ Por fim, digite seu número de identificação: ")

            sqlInsertAssociados = "insert into docentes (id,nome,curso,disciplinas,email_inst) values (%s,%s,%s,%s,%s)"
            valores = [id, nome, curso, disciplina, email]

            insertAssociadosNoBancoDados(conexao, sqlInsertAssociados, valores)

        elif setor == 3:
            print("\n" + "◆ Olá, " + nomeSplit[0] + "! Precisamos que compartilhe conosco algumas informações institucionais." + "\n")
            departamento = input("▶ Digite o departamento da universidade no qual você trabalha: ")
            id = input("▶ Por fim, digite o seu número de identificação: ")

            sqlInsertAssociados = "insert into colaboradores (id,nome,depart,email_inst) values (%s,%s,%s,%s)"
            valores = [id, nome, departamento, email]

            insertAssociadosNoBancoDados(conexao, sqlInsertAssociados, valores)

    else:
        print(error + "\n" +
              "De antemão, deve ser alertado que essa Ouvidoria é um sistema direcionado somente à "
              "associados do centro universitário." + "\n" + "Se esse não for o seu caso, o acesso não será permitido.")

    return nome