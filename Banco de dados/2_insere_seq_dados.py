import sqlite3

banco = sqlite3.connect(':memory:')
banco = sqlite3.connect('TESTE.db')#CRIA O BANCO DE DADOS "TESTE"

cursor = banco.cursor()#CURSOR É UM IDENTIFICADOR DE ARQUIVOS, PARECIDO COM CHAMAR OPEN()

listaestudantes = [('2', 'Felipe', '18', 'felipe@xyz.com', '1'), ('3', 'Carlos', '20', 'carlos@xyz.com', '3'), ('4', 'Fernanda', '30', 'fernanda@xyz.com', '4'),
('5', 'João', '19', 'joao@xyz.com', '4'),('6', 'Carla', '21', 'carla@xyz.com', '5'),('7', 'Antony', '51', 'antony@xyz.com', '6'),
('8', 'Bea', '2', 'bea@xyz.com', '33'), ('9', 'Breno', '34', 'breno@xyz.com', '5'),('10', 'Luana', '25', 'luana@xyz.com', '6')]

cursor.executemany("""INSERT INTO estudantes VALUES (?,?,?,?,?)""", listaestudantes) #insere todos os dados dentro da tabela
print("dados inseridos com sucesso!")
banco.commit()

#consultar os dados que acabou de inserir

cursor.execute("SELECT * FROM estudantes")
print(cursor.fetchall())
print(("dados inseridos com sucesso!"))
