import numpy as np

#criando arrays apenas com numeros zeros automaticamente
def matrizZeros():
    zeros = np.zeros((2, 3)) #define as dimensões, duas linhas e 3 colunas
    print(zeros)
    print("Tam da matriz: ", zeros.shape)
    print("Dimensões: ", zeros.ndim)

#driando arrayz apenas com numeros "um" automaticamente
def matrizUm():
    ones_array = np.ones((3, 5), dtype=np.int32) #especificando dtype
    print(ones_array)

def matrizId(): #criando uma matriz identidade
    #matriz com 1 na diagonal e o resto é 0
    identidade = np.eye(5) #define  tamanho da matriz
    print(identidade)

def matrizEsp(): #definindo uma matriz com numeros uniformemente espaçados
    esp = np.linspace(0, 10, 10)
    print(esp)

def arrayRange():#cria um array com n° de elementos definidos
    a = np.arange(15)
    print(a)

'''arrays podem ser utilizados de fatiamentos para retornar seus elementos
como em listas normais de python [] e podem ser modificados atraves de atribuição'''

def arrayRange2(): #cria um array com elementos de 0 a 30 espaçados de 3 em 3
    a = np.arange(0, 30, 3)
    print(a)


def reshapeMatriz():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    b = np.array(a)
    #pode utilizar reshape para redefinir a matriz
    b = np.arange(50).reshape(5,10)
    print(b)
    print('')
    #imprimindo as linhas específicas
    # primeiro colchete -> linhas
    # segundo colchete -> coluna
    print(b[:4][:]) #imprime até a linha 4

reshapeMatriz()