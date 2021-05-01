def A1():
    Lprimos=[]
    for j in range(2,1000):
        cont=0
        for i in range (1,j):
            if j%i==0:
                cont+=1
        if cont<2:
            Lprimos.append(j)
    #print (lista)
    #apenas para verificar a lista visualmente


    seguir='S'
    while seguir != 'N' and seguir != 'n':
        x=int(input("Digite um valor até 1000 para verificar: "))
        if Lprimos.count(x)> 0:
            print ("O número ", x, " é primo")
        else:
            print ("O número ", x, " não é primo")

        seguir=input("Continuar? S/N ")

    print ("Fim!")   



    
def main():
    A1()
main()
