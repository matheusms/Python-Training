import imprimir
import multiplicar


def vezes():
    y=int(input("Valor 1: "))
    z=int(input("valor 2: "))
    multiplicar.mult(y, z)

def string():
    x=input("digite uma frase: ")
    #letra a, imprimir a frase do usuário
    imprimir.imprimir(x)

def main():
    string()
    vezes()

    
    
main()


