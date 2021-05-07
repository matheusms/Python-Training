import sqlite3

banco = sqlite3.connect(':memory:')
banco = sqlite3.connect('TESTE.db')#CRIA O BANCO DE DADOS "TESTE"

cursor = banco.cursor()#CURSOR É UM IDENTIFICADOR DE ARQUIVOS, PARECIDO COM CHAMAR OPEN()

#a função SUM retorna a soma total de uma coluna numérica

SQL = """SELECT SUM(idade)
FROM estudantes
WHERE idade > 18"""

cursor.execute(SQL)
print(cursor.fetchall())