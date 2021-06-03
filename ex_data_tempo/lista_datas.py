import datetime

def lista_datas():
    day_delta = datetime.timedelta(days=1) #passo de dias
    start_date = datetime.date(1987, 10, 16) #data inicial
    end_date = datetime.date(1987, 10, 25) #data final

    for i in range((end_date-start_date).days):
        print(start_date+i*day_delta) #imprime cada dia no intervalo

lista_datas()