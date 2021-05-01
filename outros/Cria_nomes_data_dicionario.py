#cria um dicionário onde os nomes e datas aleatórios são salvos como tuplas
#{Nome: (Email, Dia de nascimento, Mês de nascimento)}
def Q6():
    listaA={}
    nomesB=[]
    for p in range(0,1000):
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
        nomesB.append(nome)
        #print(nome) 

        #adicionando os nomes aos emails             
        email = nome.lower() + '@xyz.com.br' #email com o nome
        #print(email)

        #criando data de aniversario
        mes = random.randint(1,12)
        if (mes != 1,3,5,7,8,10,12):
            dia = random.randint(1,30)
        elif (mes == 2):
            dia = random.randint(1,28)
        else:
            dia = random.randint(1,31)

        #print(dia)
        #print(mes)

        t= email, dia, mes #criantdo tupla com os dados
        #até aqui o programa feito para 1 só
        #print(t)

        listaA[nome]=t #cria o dicionario com dados de cada nome
        
    #print(listaA)
    #print para conferir o dicionário para testes e confirmação


    dia = int(input("Selecione a dia: "))
    mes = int(input("Selecione o mês: "))

    print("Aniversariantes da data: ", dia, "/", mes, " (nome, email) ")

   
    for k, v in listaA.items():#esse for percorre k(as keys) e v(os values)
        if v[1]==dia and v[2]==mes:
            print(k,', email:', v[0])
            
     

def main():
    Q6()
main()
        

        





