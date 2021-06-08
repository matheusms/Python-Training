import matplotlib
import matplotlib.pyplot as plt

#verificando estilos de graficos disponiveis
#print(plt.style.available)

#definindo um estilo de grafico
plt.style.use('seaborn-paper')

#definindo o tamanho dos graficos
plt.rcParams['figure.figsize'] = (11,7)

#para salvar um arquivo png com transparencia
#plt.savefig('nome_da_imagem.png', transparent = True)

#eixos x e y
x = [1,2,3,4,5,6,7,8,9,10]
y=[11,12,13,14,15,16,17,18,19,20]

#imprimindo o grafico
#fig,ax = plt.subplots()
#ax.plot(x,y)
#plt.show()

#alterando o nome dos eixos
plt.xlabel('Nome do eixo X')
plt.ylabel('Nome do eixo Y')

#outra forma de criar um grafico
plt.plot(x, y)
plt.show()


