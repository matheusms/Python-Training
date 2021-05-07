import sqlite3

banco = sqlite3.connect(':memory:')
banco = sqlite3.connect('TESTE.db')#CRIA O BANCO DE DADOS "TESTE"

cursor = banco.cursor()#CURSOR É UM IDENTIFICADOR DE ARQUIVOS, PARECIDO COM CHAMAR OPEN()

#solicita que as linhas retornadas sejam classificadas por um dos campos escolhidos
cursor.execute("SELECT nomeEstudante, idDepartamento FROM estudantes GROUP BY nomeEstudante")
print(cursor.fetchall())