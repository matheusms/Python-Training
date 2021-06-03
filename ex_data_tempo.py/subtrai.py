import datetime

def dif_data():
    day_delta = datetime.timedelta(days=1) #marcador de passo
    
    start_date = datetime.date(2021, 1, 25) #definindo a data do exemplo
    
    data = start_date - 8*(day_delta) #subtraindo 8 dias
    print(data)

dif_data()