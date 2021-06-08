import numpy as np
import random

#gerando arrays com numeros aleatorios
a = np.random.randint(1,3,5)
b = np.random.randint(0,10,5)

print("Array a: ", a)
print("Array b: ", b)

def subtracao():
    c = np.subtract(b, a) #subtrai os valores do array b pelo do array a
    print("subtração: ", c)

def adicao(): # soma os valores do array b com os valores do array a
    c = np.add(b, a)
    print("Adição: ", c)

def divisao(): #realiza a divisão dos arrays a pelo b
    c = np.divide(a, b)
    print("Divisão: ", c)

def multiplicacao(): #realiza a multiplicação entre os valores dos arrays
    c = np.multiply(a, b)
    print("Multiplicação: ", c)

def exponecial(): #retorna os valores exponenciais de um dado array
    c = np.exp(a)
    print("Exponencial: ", c)

def raiz(): #retorna as raizes dos valores do array dado
    c = np.sqrt(a)
    print("Raiz: ", c)

def seno(): #retorna o seno dos valores do array
    c = np.sin(a)
    print("Seno: ", c)

def logaritimo(): #retorna o log dos valores do array
    c = np.log(a)
    print("Log: ", c)

def logaritimo2():#retorna o log na base 2 dos valores do array
    c = np.log2(a)
    print("Log2: ", c)

def arredondar(): #arredondar matriz
    c = np.random.seed(42)
    d = np.random.rand(5)
    print(d)
    e = np.around(d)
    print(e)

arredondar()