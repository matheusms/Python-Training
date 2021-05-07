#criando comando para alterar um dado no banco
#OBS: não esquecer de dar commit para confirmar a mudança
import sqlite3

banco = sqlite3.connect(':memory:')
banco = sqlite3.connect('TESTE.db')#CRIA O BANCO DE DADOS "TESTE"

cursor = banco.cursor()#CURSOR É UM IDENTIFICADOR DE ARQUIVOS, PARECIDO COM CHAMAR OPEN()

#todos os registros de 'FELIPE' serão alterados para 'DIEGO' 
SQL = """
UPDATE estudantes
SET nomeEstudante = 'Felipe'
WHERE nomeEstudante = 'Diego'
"""

cursor.execute(SQL)
banco.commit()
print("Registro atualizado!")

#consultando os dados
cursor.execute("SELECT * FROM estudantes")
print(cursor.fetchall())
