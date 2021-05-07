"""CRIANDO BANCO DE DADOS ATRAVÉS DO SQLITE3 BÁSICO"""
import sqlite3
#INSTALAR SQLITE3


banco = sqlite3.connect(':memory:')
banco = sqlite3.connect('TESTE.db')#CRIA O BANCO DE DADOS "TESTE"

cursor = banco.cursor()#CURSOR É UM IDENTIFICADOR DE ARQUIVOS, PARECIDO COM CHAMAR OPEN()

#CRIA UMA TABELA DE DADOS
cursor.execute("CREATE TABLE estudantes (idEstudante integer, nomeEstudante text, idade integer, email text, idDepartamento integer)")
#ADICIONA OS DADOS NA TABELA
cursor.execute("INSERT INTO estudantes VALUES(1, 'Maria', 40, 'maria@xyz.com', 2)")
#COMMIT FAZ AS CONFIRMAÇÕES
banco.commit()

cursor.execute("SELECT * FROM estudantes")#CONSULTA DADOS NA TABELA 'ESTUDANTES'
print(cursor.fetchall())#RETORNA AS TABELAS DE DADOS

