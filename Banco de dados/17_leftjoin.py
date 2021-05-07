import sqlite3

banco = sqlite3.connect(':memory:')
banco = sqlite3.connect('TESTE.db')#CRIA O BANCO DE DADOS "TESTE"

cursor = banco.cursor()#CURSOR É UM IDENTIFICADOR DE ARQUIVOS, PARECIDO COM CHAMAR OPEN()

SQL = """SELECT
    estudantes.nomeEstudante,
    departamentos.nomeDepartamento
FROM estudantes
LEFT JOIN departamentos ON estudantes.idDepartamento = departamentos.idDepartamento"""
#Estudantes é a tabela da esquerda 

cursor.execute(SQL)
print(cursor.fetchall())
