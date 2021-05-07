import sqlite3

banco = sqlite3.connect(':memory:')
banco = sqlite3.connect('TESTE.db')#CRIA O BANCO DE DADOS "TESTE"

cursor = banco.cursor()#CURSOR É UM IDENTIFICADOR DE ARQUIVOS, PARECIDO COM CHAMAR OPEN()

#seleciona dados da tabela onde a idade é especificada
cursor.execute("""SELECT * FROM estudantes
WHERE idade = '34'""")
print(cursor.fetchall())

#essa consulta NÃO altera os dados da tabela
#pode ser usado para cada item da tabela, como nome, idade, email... 
