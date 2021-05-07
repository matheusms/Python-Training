import sqlite3

banco = sqlite3.connect(':memory:')
banco = sqlite3.connect('TESTE.db')#CRIA O BANCO DE DADOS "TESTE"

cursor = banco.cursor()#CURSOR É UM IDENTIFICADOR DE ARQUIVOS, PARECIDO COM CHAMAR OPEN()

SQL = """SELECT
    estudantes.nomeEstudante,
    departamentos.nomeDepartamento
FROM departamentos
INNER JOIN estudantes ON estudantes.idDepartamento = departamentos.idDepartamento"""
#na tabela de estudantes o id tem que ser igual na tabela de departamentos

cursor.execute(SQL)
print(cursor.fetchall())
