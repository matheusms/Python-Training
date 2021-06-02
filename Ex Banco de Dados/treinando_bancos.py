import sqlite3

def LetraA(cursor): #listar nopme e sobrenome ordenado por sobrenome
    
    cursor.execute("""SELECT PrimeiroNome, UltimoNome FROM funcionarios
    ORDER BY UltimoNome""")

    print(cursor.fetchall())

def LetraB(cursor): #listar todos os campos de funcionarios ordenados por cidade
    cursor.execute("""SELECT * FROM funcionarios
    ORDER BY Cidade""")
    print(cursor.fetchall())

def LetraC(cursor): #lista de func que tem salario maior que 1000 ordenado por idade
    cursor.execute("""SELECT * FROM funcionarios
    WHERE Salario > 1000
    ORDER BY PrimeiroNome, SegundoNome, UltimoNome""")
    print(cursor.fetchall())

def LetraD(cursor): #lista ordenada por idade
    cursor.execute("""SELECT DataNasci, PrimeiroNome FROM funcionarios
    ORDER BY DataNasci DESC, PrimeiroNome""")
    print(cursor.fetchall())

def LetraE(cursor): #lista total da folha de pagamento
    cursor.execute("""SELECT SUM(Salario) FROM funcionarios""")
    print(cursor.fetchall())

def LetraF(cursor): #lista nome, dep e função de todos os funcionarios
    cursor.execute("""SELECT funcionarios.PrimeiroNome, departamentos.Nome,
    funcionarios.funcao
    FROM funcionarios JOIN departamentos
    ON funcionarios.CodigoDepartamento = departamentos.Codigo
    ORDER BY funcionarios.PrimeiroNome""")
    print(cursor.fetchall())

def LetraG(cursor): #lista quantidade de funcionarios da empresa
    cursor.execute("""SELECT COUNT(*) FROM funcionarios""")
    print(cursor.fetchall())

def LetraH(cursor): #lista nome de dep e do funcionario ordenado por departamento
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