import sqlite3

banco = sqlite3.connect(':memory:')
banco = sqlite3.connect('TESTE.db')#CRIA O BANCO DE DADOS "TESTE"

cursor = banco.cursor()#CURSOR É UM IDENTIFICADOR DE ARQUIVOS, PARECIDO COM CHAMAR OPEN()

#selecionando dados com operdor AND, nome e idade especificos
cursor.execute("""SELECT * FROM estudantes WHERE nomeEstudante = 'Felipe' AND idade = '18'""")
print((cursor.fetchall()))
#se não satisfazer esse AND ele retorna vazio []