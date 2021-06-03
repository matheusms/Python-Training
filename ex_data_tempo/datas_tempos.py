import time



def datas():
    today = time.localtime()
    print("Data e hora atual: ", time.ctime())
    #ano = time.strftime("%Y", today)
    print("Ano: ", time.strftime("%Y", today))
    print("Mês: ", time.strftime("%m", today))
    print("N° da semana do ano: ", time.strftime("%U", time.localtime()))
    print("Dia atual da semana: ", time.strftime("%A", time.localtime()))
    print("Dia do ano: ", time.strftime("%j", time.localtime()))
    print("Dia do mês: ", time.strftime("%d", time.localtime()))
    print("Dia da semana (domingo=0): ", time.strftime("%w", time.localtime()))
  

datas()