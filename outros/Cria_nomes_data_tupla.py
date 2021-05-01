#cria nomes e datas aleatórias em uma tupla e depois verifica se esta na lista
def criarNomes():
    lista=[]
    for p in range(0,100):
        import random
        num = random.randint(3,10)
        #coloquei de 3 a 10 para nao ficar com nomes de 1 letra só
        #print(num)

        #criando nomes aleatórios
        nome=''
        primLetra = random.randint(65,90)
        nome=nome+chr(primLetra)
        for k in range(num):
            r = random.randint(97,122)
            nome = nome + chr(r)
        #print(nome)
                 
        email = nome.lower() + '@xyz.com.br' #email com o nome
     
        #print(nome)
        #print(email)

        mes = random.randint(1,12)
        if (mes != 1,3,5,7,8,10,12):
            dia = random.randint(1,30)
        elif (mes == 2):
            dia = random.randint(1,28)
        else:
            dia = random.randint(1,31)

        #print(dia)
        #print(mes)

        t= nome, email, dia, mes
        #até aqui o programa feito para 1 só
        #print(t)

        
        lista.append(t)
    
    #print(lista)
    #apenas para checar nos testes

    
    data1 = int(input("Selecione a dia: "))
    data2 = int(input("Selecione o mês: "))
    
    cont=0
    print("Aniversariantes desta data: ", data1, "/", data2, " (nome, email) ")
    for b in lista:

        if (data2 in b[3:4:]):
            if (data1 in b[2:3:]):
                print("Nome: ", b[0], ", email: ", b[1])
                cont+=1

    if (cont == 0):
        print('Não existe aniversariante nesta Data')
    

        
        
def main():
    criarNomes()
main()
