import sqlite3

banco = sqlite3.connect(':memory:')
banco = sqlite3.connect('TESTE.db')#CRIA O BANCO DE DADOS "TESTE"

cursor = banco.cursor()#CURSOR É UM IDENTIFICADOR DE ARQUIVOS, PARECIDO COM CHAMAR OPEN()

SQL = """
DROP TABLE departamentos
"""

cursor.execute(SQL)
banco.commit()
print("Tabela Deletada!")

#ocorre erro ao tentar ver a tabela pois ela não existe mais
#cursor.execute("SELECT * FROM departamentos")
#print(cursor.fetchall())