import pandas as pd

path = r'D:\diretório do documento\meu_arquivo_excel.xlsx'
xlsx = pd.ExcelFile(path)
dfs = pd.read_excel(xlsx, sheet_name='Planilha1')
print(dfs) #imprimindo a planilha

