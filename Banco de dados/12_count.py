import sqlite3

banco = sqlite3.connect(':memory:')
banco = sqlite3.connect('TESTE.db')#CRIA O BANCO DE DADOS "TESTE"

cursor = banco.cursor()#CURSOR É UM IDENTIFICADOR DE ARQUIVOS, PARECIDO COM CHAMAR OPEN()

#a função COUNT retorna o número de linhas que correspondem a um critério especificado

SQL = """SELECT COUNT(nomeEstudante)
FROM estudantes
WHERE nomeEstudante = 'Maria'"""

cursor.execute(SQL)
print(cursor.fetchall())