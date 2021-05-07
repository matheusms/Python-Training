import sqlite3

banco = sqlite3.connect(':memory:')
banco = sqlite3.connect('TESTE.db')#CRIA O BANCO DE DADOS "TESTE"

cursor = banco.cursor()#CURSOR É UM IDENTIFICADOR DE ARQUIVOS, PARECIDO COM CHAMAR OPEN()

#seleciona dados de um ou de outra especificação
cursor.execute("""SELECT * FROM estudantes WHERE nomeEstudante = 'Maria' OR idade ='18'""")
print(cursor.fetchall())
#ou retorna maria ou alguem com idade 18 ou os dois