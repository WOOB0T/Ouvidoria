# FUNÇÕES IMORTADAS:

from def1nome import *
from listarPorCategoria import *
from insert import *
from def4nome import *
from consultarPeloCodigo import *
from def6nome import *
from def7nome import *
from operacoesbd import *


# VARIAVÉIS DE MENSAGENS AUTOMÁTICAS:
loading = "↻ Carregando..."
acesso = "Acesso liberado! 🐍"
redirect = "Iremos te redirecionar para o menu principal."
error = "⚠︎ A opção inserida é inválida! ⚠︎"


# 0 - CATEGORIAS (SOMENTE POR QUESTÃO DE ORGANIZAÇÃO)
def categoriasOcorrencias():
    print("\n" + "◆ Categorias de Manifestações:" + "\n")
    print("[ 1 ] Reclamações")
    print("[ 2 ] Sugestões")
    print("[ 3 ] Elogios" + "\n")