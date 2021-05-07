import sqlite3

banco = sqlite3.connect(':memory:')
banco = sqlite3.connect('TESTE.db')#CRIA O BANCO DE DADOS "TESTE"

cursor = banco.cursor()#CURSOR É UM IDENTIFICADOR DE ARQUIVOS, PARECIDO COM CHAMAR OPEN()


#ASC -> ordem crescente
#DESC -> ordem decrescente

cursor.execute("SELECT nomeEstudante, idade FROM estudantes ORDER BY idade ASC")
print(cursor.fetchall())