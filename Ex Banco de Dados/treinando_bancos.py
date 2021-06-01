import sqlite3

def LetraA(cursor):
    
    cursor.execute("""SELECT PrimeiroNome, UltimoNome FROM funcionarios
    ORDER BY UltimoNome""")

    print(cursor.fetchall())

def LetraB(cursor):
    cursor.execute("""SELECT * FROM funcionarios
    ORDER BY Cidade""")
    print(cursor.fetchall())

def LetraC(cursor):
    cursor.execute("""SELECT * FROM funcionarios
    WHERE Salario > 1000
    ORDER BY PrimeiroNome, SegundoNome, UltimoNome""")
    print(cursor.fetchall())

def LetraD(cursor):
    cursor.execute("""SELECT DataNasci, PrimeiroNome FROM funcionarios
    ORDER BY DataNasci DESC, PrimeiroNome""")
    print(cursor.fetchall())

def LetraE(cursor):
    cursor.execute("""SELECT SUM(Salario) FROM funcionarios""")
    print(cursor.fetchall())

def LetraF(cursor):
    cursor.execute("""SELECT funcionarios.PrimeiroNome, departamentos.Nome,
    funcionarios.funcao
    FROM funcionarios JOIN departamentos
    ON funcionarios.CodigoDepartamento = departamentos.Codigo
    ORDER BY funcionarios.PrimeiroNome""")
    print(cursor.fetchall())

def LetraG(cursor):
    cursor.execute("""SELECT COUNT(*) FROM funcionarios""")
    print(cursor.fetchall())

def LetraH(cursor):
    cursor.execute("""SELECT departamentos.nome, funcionarios.PrimeiroNome
    FROM departamentos JOIN
    funcionarios ON departamentos.Codigo = funcionarios.codigoDepartamento
    ORDER BY departamentos.Nome, funcionarios.PrimeiroNome""")
    print(cursor.fetchall())

def main():
    banco = sqlite3.connect(':memory:')
    banco = sqlite3.connect('banco_teste.db')
    cursor = banco.cursor()

    #retirar cada # para executar cada letra <-----------

    #LetraA(cursor) 
    #LetraB(cursor) 
    #LetraC(cursor)
    LetraD(cursor)
    #LetraE(cursor)
    #LetraF(cursor)
    #LetraG(cursor)
    #LetraH(cursor)


main()