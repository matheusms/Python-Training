import datetime

def data_qualquer():
    #armazena uma data específica
    umadata = datetime.date(2021,2,8)
    print(umadata.day) #imprime o dia da data definida acima

def data_atrib():
    #atribui data e hora, min e seg
    print(datetime.datetime(2021,1,2,4,20,34,565))

def dia_hoje(): #armazenando a data de hoje
    hoje = datetime.date.today()
    print("Data: ", hoje)
    print("Dia: ", hoje.day)
    print("Mês: ", hoje.month) 
    print("Ano: ", hoje.year)
    print("Dia da semana: ", hoje.weekday()) #segunda feira = 0 e domingo = 6
    print("Dia da semana: ", hoje.isoweekday()) #segunda feira = 1 e domingo = 7
    
def now_day():
    y = datetime.datetime.now()
    print("Data e hora: ", y)
    print("Ano: ", y.year)
    print("Mês: ", y.month)
    print("Dia: ", y.day)
    

now_day()
