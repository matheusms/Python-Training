import sqlite3

#criando o banco de dados
banco = sqlite3.connect('banco_teste.db')

cursor = banco.cursor()

#criando a tabela
cursor.execute("CREATE TABLE funcionarios (Codigo integer, PrimeiroNome text, SegundoNome text, UltimoNome text, DataNasci date, CPF integer, RG integer, Endereco text, CEP integer, Cidade text, Fone integer, CodigoDepartamento integer, Funcao text, Salario integer)")

listafun = [('1', 'Matheus', 'Felipe', 'Santos', '11/02/1998', '13456', '12344', 'Alvieira, 22', '21982070', 'RJ', '111111111', '1', 'Engenheiro', '4000'), 
('2', 'João', 'Lucas', 'Pereira', '1/05/1990', '23345', '22334', 'Menezes, 42', '2134560', 'SP', '222222222', '2', 'Técnico', '2000'),
('3', 'Claudio', 'Almeira', 'Santos', '12/01/1988', '23546', '22344', 'Alabastra, 50', '21432570', 'SC', '333333333', '3', 'Diretor', '7000'),
('4', 'Camila', 'Felicio', 'Silva', '29/10/2000', '54231', '55634', 'Muniz, 10', '21532340', 'PB', '444444444', '2', 'Técnico', '2000'),
('5', 'Luana', 'Camelo', 'Brito', '26/07/1996', '45678', '75665', 'Ricardo, 12', '21324660', 'RS', '555555555', '4', 'Engenheiro', '4000'),
('6', 'Rayssa', 'Dias', 'Ferras', '5/06/1995', '56743', '32211', 'Andino, 65', '21323450', 'MG', '666666666', '5', 'Diretor', '8000'),
('7', 'Felipe', 'Almeida', 'Santos', '17/04/1997', '21243', '95685', 'Presidente Joao, 11', '21345640', 'MG', '777777777', '1', 'Assistente', '1000'),
('8', 'Pedro', 'Assunçao', 'Silva', '14/11/1999', '12435', '76483', 'Salino, 30', '21434560', 'RJ', '888888888', '3', 'Engenheiro', '4000'),
('9', 'Cleber', 'Diniz', 'Silva', '22/08/1994', '34556', '39847', 'Alcantara, 10', '21235460', 'RJ', '999999999', '2', 'Tecnico', '2000'),
('10', 'Juliana', 'Pereira', 'Costa', '16/12/1993', '66456', '98375', 'Sampaio, 20', '21346660', 'RJ', '989898989', '3', 'Engenheiro', '4000')]

cursor.executemany("""INSERT INTO funcionarios VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)""", listafun)

cursor.execute("CREATE TABLE departamentos (Codigo integer, Nome text, Localizacao text, CodigoFuncionarioGerente integer)")

listadep = [('1', 'Diretoria', 'bloco A', '6'), ('2', 'Pesquisa', 'bloco B', '1'), ('3', 'Manutençao', 'bloco C', '8'), ('4', 'Esconomia', 'bloco D', '10'), ('5', 'TI', 'bloco E', '4'),]

cursor.executemany("""INSERT INTO departamentos VALUES (?,?,?,?)""", listadep)

banco.commit()

