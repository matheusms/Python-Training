#descobrir o tipo do triângulo
def Q1():

    A = int (input("Insira o lado A: "))
    B = int (input("Insira o lado B: "))
    C = int (input("Insira o lado C: "))

    if A+B>C and A+C>B and B+C>A:
        
        if (A == B == C) :
            print ("ABC é um triângulo equilátero")
        elif A == B and B!=C:
            print ("ABC é um triângulo isósceles")
        elif A == C and C!=B:
            print ("ABC é um triângulo isósceles")
        elif B == C and C!=A:
            print ("ABC é um triângulo isósceles")
        else:
            print ("ABC é um triângulo escaleno")

    else:
        print ("ABC não formam um triângulo")

def main ():
    Q1()
main ()
