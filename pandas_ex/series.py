#importando o pandas
import pandas as pd

#iniciando e imprimindo uma serie
s = pd.Series([3, -5, 7, 4], index=['a', 'b', 'c', 'd']) #indexador pode ser numérico também

print(s)

#é possivel acessar atraves do indexador 
print('Linha b: ', s['b'])

#removendo linhas pelo index
print(s.drop('a'))