#exercicio 1

lista=[]

def dados():
    a=input("nome: ")
    b=input("sexo(H/M): ")
    b=b.upper()
    c=int(input("idade: "))
    dadosD={"nome": a, "sexo": b, "idade": c}
    return dadosD

def entrada():
    print('I - insere dados')
    print('F - fim')
    x = input('o que deseja: ')
    x=x.upper()
    while (x == 'I'):
        lista.append(dados())
        x = input('o que deseja: ')
        x=x.upper()
    return lista
    
def pessoas():
    print("o numero de pessoas cadastradas é: ", len(lista))
        
def idadeM():
    soma=0
    for i in lista:
        soma+=i["idade"]
    media=soma/len(lista)
    return media

def mulher():
    listaM=[]
    for i in lista:
        if (i["sexo"]=="M"):
            listaM.append(i)
    return listaM

def acimaM():
    
    listaA=[]
    for i in lista:
        j=i["idade"]
        if(j>idadeM()):
            listaA.append(i)
    return listaA

def main():
    entrada()
    pessoas()
    print("A média de idade é: ", idadeM())
    #print(lista)
    print("Mulheres: ", mulher())    
    print("Idades acima da média: ", acimaM())
main()
    
