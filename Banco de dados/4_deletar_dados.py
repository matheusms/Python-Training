import sqlite3

banco = sqlite3.connect(':memory:')
banco = sqlite3.connect('TESTE.db')#CRIA O BANCO DE DADOS "TESTE"

cursor = banco.cursor()#CURSOR É UM IDENTIFICADOR DE ARQUIVOS, PARECIDO COM CHAMAR OPEN()

SQL = """
DELETE FROM estudantes
WHERE nomeEstudante = 'Maria'
"""

cursor.execute(SQL)
banco.commit()
print("Registros deletados!")

#consultando os dados
cursor.execute("SELECT * FROM estudantes")
print(cursor.fetchall())