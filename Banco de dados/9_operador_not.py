import sqlite3

banco = sqlite3.connect(':memory:')
banco = sqlite3.connect('TESTE.db')#CRIA O BANCO DE DADOS "TESTE"

cursor = banco.cursor()#CURSOR É UM IDENTIFICADOR DE ARQUIVOS, PARECIDO COM CHAMAR OPEN()

#seleciona todos os dados diferente do especificado
cursor.execute("""SELECT * FROM estudantes WHERE NOT nomeEstudante = 'Maria' OR idade = '18'""")
print(cursor.fetchall())