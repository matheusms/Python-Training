import pandas as pd

#lendo arquivo csv e definindo o iso 
path = r"D:\diretorio do documento\meu_arquivo.csv"
df = pd.read_csv(path, encoding='ISO-8859-1')

df.to_csv() #escrevendo e salvando um arquivo do tipo csv

print(df)