from datetime import datetime
from datetime import timedelta

def lista_datas():
    #definindo tamanho de cada passo em dias
    day_delta = datetime.timedelta(days=1)

    start_date = datetime.date.today() #data inicial -> data de hoje
    end_date = start_date + 5*day_delta #5 dias no passo 1

    for i in range((end_date - start_date).days):
        print(start_date + i*day_delta)
        #imprime as datas entre final e inicial
    
def dif_data():
    b1 = datetime.timedelta(days=25)
    b2 = datetime.timedelta(days=15)
    b3 = b2 - b1
    print("A diferença de datas é: ", b3)
    print(type(b3))

def dif_today():
    #calcular diferença de dias entre uma data especifica e a data atual
    now = datetime.now()
    then = datetime(2019, 5, 23)
    delta = now-then
    print(delta)

def dif_amanha_ontem(): #imprimindo a diferença entre amanha e ontem
    today = datetime.date.today() #define o dia de hoje
    print("Hoje: ", today)

    yesterday = today - datetime.timedelta(days=1)#definindo o dia de ontem
    print("Ontem: ", yesterday)

    tomorrow = today + datetime.timedelta(days=1)#definindo o dia de amanha
    print("Amanhã: ", tomorrow)

    print("Tempo entre amanha e ontem: ", tomorrow - yesterday)

def convert_string(): #convertendo string no formato data e tempo
    texto = '2021-02-08'
    y = datetime.strptime(texto, '%Y-%m-%d')
    print("Data: ", y)
    z = datetime.now()
    diff = z - y
    print(diff)

convert_string()


