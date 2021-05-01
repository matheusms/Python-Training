#lista de contatos salvando em arquivo txt
L=[]

#carrega o arquivo txt em uma lista para rodar
def carregar():
    f=open('lista.txt','r')
    x1=f.readlines()
    for i in x1:
        t1 = i.split('\n')
        L1=t1[0].split(' ')
        t = L1[0], L1[1], L1[2], L1[3]
        L.append(t)   

#salva a lista no arquivo txt    
def salvar():
    f=open('lista.txt','w')

    for i in L:
        aux2=(i[0]+ ' '  + i[1] + ' ' + i[2] + ' ' + i[3] + '\n')
        f.write(aux2)
    f.close()
    

def incluir():
    nome = input("Nome: ")
    nome = nome.lower()
    email = nome.lower() + "@xyz.com.br"
    dia = (input("Dia: "))
    mes = (input("Mês: "))
    t = nome, email, dia, mes
    L.append(t)

def consultar():
    cont1=0
    if (len(L)==0):
        print("Ainda não existe nome listado!")
    else:
        j = input("Nome a consultar: ")
        for b in L:
            if (j.lower() in b):
                cont1+=1
                print("Nome:", b[0], ", email:", b[1], ", aniversário: ", b[2],"/",b[3])
        if(cont1==0):
            print("Não existe ninguém com o nome '", j,"'")

def consultar_aniversariante():
    cont=0
    if (len(L)==0):
        print("Ainda não existe nome listado!")
    else:
        dia = (input("Selecione a dia: "))
        mes = (input("Selecione o mês: "))
        for b in L:
            if (mes == b[3]):
                if (dia == b[2]):
                    print("Nome:", b[0], ", email:", b[1], "data: ", b[2],"/",b[3])
                    cont+=1

        if (cont == 0):
            print('Não existe aniversariante nesta Data', dia, '/', mes)

def listar():
    if (len(L)==0):
        print("Ainda não existe nome listado!")
    else:
        for x in L:
            print("nome:",x[0], ", email:", x[1], ", aniversário: ", x[2],"/",x[3])
def opcao():
    print('Incluir(I)')
    print('Consultar(C)')
    print('Consultar Aniversariante(CA)')
    print('Listar(L)')
    print('Fim(F)')



def main():
    carregar()
    opcao()
    
    w = "S"
    while (w == "S"):
        z = input("Selecione uma opção: ")
        if (z.upper() == 'I'):
            incluir()
        elif (z.upper() == 'C'):
            consultar()
        elif (z.upper() == 'CA'):
            consultar_aniversariante()
        elif (z.upper() == 'L'):
            listar()
        elif (z.upper() == "F"):
            w = "n"
        else:
            print("Opção inválida, tente novamente!")
    print("FIM!")
    salvar()
            
       
main()

