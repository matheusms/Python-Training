def teste_erros():
    try:
        a=int(input("insira um número: "))
        b=int(input("insira um número: "))

    except ValueError: #reconhece se não for inserido um número
        print("Ops, não é um número. Insira números e inteiros")

    else:
        x=input("qual operação deseja: soma(+),subtração(-),multiplicação(*) ou divisão(/)? ")
        if (x=="+"):
            c=a+b
        elif(x=="-"):
            c=a-b
        elif(x=="*"):
            c=a*b
        elif(x=="/"):
            c=a/b
        else:
            print("Operação inválida! Tente novamente!!!")
            x=input("qual operação deseja: soma(+),subtração(-),multiplicação(*) ou divisão(/)? ")
            if (x=="+"):
                c=a+b
            elif(x=="-"):
                c=a-b
            elif(x=="*"):
                c=a*b
            elif(x=="/"):
                c=a/b
    
    finally:
        print("O resultado é: ", c)
    


def main():
    teste_erros()

main()