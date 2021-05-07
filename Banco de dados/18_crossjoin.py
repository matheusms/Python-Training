import sqlite3

banco = sqlite3.connect(':memory:')
banco = sqlite3.connect('TESTE.db')#CRIA O BANCO DE DADOS "TESTE"

cursor = banco.cursor()#CURSOR É UM IDENTIFICADOR DE ARQUIVOS, PARECIDO COM CHAMAR OPEN()


"""cross join fornece um produto cartesiano para as colunas selecionadas das duas tabelas unidas, combinando todos os valores da primeira
tabela com os valores da segunda tabela"""

SQL = """SELECT
    estudantes.nomeEstudante,
    departamentos.nomeDepartamento
FROM estudantes
CROSS JOIN departamentos"""
#na tabela de estudantes o id tem que ser igual na tabela de departamentos

cursor.execute(SQL)
print(cursor.fetchall())
#mostra todas as combinações possiveis que cada item da tabela pode possuir