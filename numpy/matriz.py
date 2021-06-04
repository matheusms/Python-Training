#criando arrays multidimensionais
import numpy as np

lista = [[1, 2, 3], [3, 4, 5]]
b = np.array(lista)
print(b)

print(b.shape) #tamanho da matriz (linha, coluna)
print(b.ndim) #retorna a dimensão da matriz