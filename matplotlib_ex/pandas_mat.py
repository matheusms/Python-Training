import pandas as pd
import matplotlib.pyplot as plt

#criando e imprimindo um DataFrame
data = { 
    'x' : [1,2,3,4,5,6,7,8,9,10],
    'y' : [11,12,13,14,15,16,17,18,19,20]
}
df = pd.DataFrame(data, columns=['x','y'])
#print(df)

#para plotar todas as colunas ou variaveis do dataframe
df.plot()
plt.title('Titulo do Gráfico')#adicionando o titulo
#alterando o nome dos eixos
plt.xlabel('Nome do eixo X')
plt.ylabel('Nome do eixo Y')
plt.show()

x = [1,2,3,4,5,6,7,8,9,10]
y=[11,12,13,14,15,16,17,18,19,20]
#alterando o tipo de gráfico
plt.bar(x,y) #gráfico de barras
plt.show()

plt.pie(x,y) #grafico de pizza
plt.show()

plt.scatter(x,y) #grafico de dispersão
plt.show()

#criando um grafico com legenda de cor das barras
plt.bar(x,y, color = '#55a589', label = 'Legenda')
plt.legend() #é possivel mudar a posição da legenda plt.legend(loc='best')
plt.show()

#é possivel colocar dois graficos juntos
plt.plot(x,y, color = 'green')
plt.scatter(x, y, color ='red')
plt.show()