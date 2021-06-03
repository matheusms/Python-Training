import datetime

def dif_data():
    dia1 = datetime.timedelta(days=11)
    dia2 = datetime.timedelta(days=1)
    diff = dia2 - dia1
    print("A diferença de datas é: ", diff)
    

dif_data()