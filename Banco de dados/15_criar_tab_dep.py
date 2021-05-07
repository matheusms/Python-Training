"""criar uma tabela departamentos para conectar essa tabela com a de estudantes através do idDepartamento"""

import sqlite3

banco = sqlite3.connect(':memory:')
banco = sqlite3.connect('TESTE.db')#CRIA O BANCO DE DADOS "TESTE"

cursor = banco.cursor()#CURSOR É UM IDENTIFICADOR DE ARQUIVOS, PARECIDO COM CHAMAR OPEN()

#criando a tabela "departamentos" com idDepartamento, nomeDepartamento
cursor.execute("CREATE TABLE departamentos (idDepartamento integer PRIMARY KEY , nomeDepartamento text)")
print("Tabela criada!")

#inserir dados na tabela
listadepartamento = [('1', 'TI'), ('2', 'Física'), ('3','Matemárica'), ('4', 'Engenharia'), ('5', 'Biologia'), ('6', 'Historia')]

#inserir os dados na tabela
cursor.executemany("""INSERT INTO departamentos VALUES (?,?)""", listadepartamento)
print("dados inseridos!")
banco.commit()

cursor.execute("SELECT * FROM departamentos")
print(cursor.fetchall())