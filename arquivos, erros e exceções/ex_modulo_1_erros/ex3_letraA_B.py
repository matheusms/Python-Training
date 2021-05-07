
def teste_erros():
    try:
        a=int(input("insira um número: "))
        b=int(input("insira um número: "))
        x=input("qual operação deseja: soma(+),subtração(-),multiplicação(*) ou divisão(/)?")
        if (x=="+"):
            print(a+b)
        elif(x=="-"):
            print(a-b)
        elif(x=="*"):
            print(a*b)
        else:
            print(a/b)
    except ValueError:
        print("Ops, não é um número. Insira números e inteiros")

    


def main():
    teste_erros()

main()