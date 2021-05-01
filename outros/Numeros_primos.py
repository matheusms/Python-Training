#descobre se um numero n é primo e retorna todos os primos até o numero n
def AllPrimo():
    n=int(input("Digite um numero: "))
    cont=0
    for i in range (2,n):
        if n%i==0:
            cont+=1
    if cont>=2:
        print (n, " não é um numero primo")
    else:
        print (n, " é primo")
    
    print ("Números primos até ", n, ": ")
    for j in range(2,n):
        cont=0
        for i in range (2,j+1):
            if j%i==0:
                cont+=1
        if cont<2:
            print (j)
    
    


def main():
    AllPrimo()
main()
