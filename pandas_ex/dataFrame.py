import pandas as pd

#iniciando o DataFrame

data = {'País' : ['Bélgica', 'Índia', 'Brasil'], 'Capital' : ['Bruxelas', 'Nova Delhi', 'Brasilia'], 'População': [12345, 456789, 987654]}

df = pd.DataFrame(data, columns = ['País', 'Capital', 'População'])

print(df)
print('')

#para ver o começo do conteudo de um DataFrame
print(df.head())
print('')

#para recuperar um subconjunto de um DataFrame
print(df[1:]) #apartir do indice 1
print('')

#recuperando um unico valor atraves da linha e coluna
print(df.loc[[0],['País']])
print('')

#removendo coluna
print(df.drop('País', axis=1)) 
print('')

#quantidade de linhas e colunas
print("Linhas e colunas: ", df.shape)
print('')

#colunas presentes no DataFrame
print(df.columns)
print('')

#contagem de dados não-nulos
print(df.count())
print('')

#descrição do index
print(df.index)
print('')

#adicionando uma nova coluna
df['Nova Coluna'] = 0
print(df)
print('')
#renomeando colunas
df.columns = ['Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4']
print(df)
print('')
#renomeando colunas específicas
df.rename({'País' : 'Coluna 1', 'Capital': 'Coluna 2', 'População' : 'Coluna 3', 'Nova Coluna' : 'Coluna 4'})
print(df)