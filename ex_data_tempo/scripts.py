#impressão trabalhando com o tempo da época padrao 1 de jan de 1970
import time

def impressao():
    #época padrao 
    padrao = time.strftime("%Y-%m-%d-%H.%M.%S", time.gmtime(0))
    print("Época padrão: ", padrao)

    #segundos desde a época padrao
    seconds = time.time()
    print("Segundos desde a época: ", seconds)

    #tempo atual
    print("Tempo local: ", time.asctime())

    #objeto time.localtime()
    obj = time.localtime()
    print("Hora:minn:seg ->", obj[3:6])

    #horario de verão ou não
    if obj[8] == 0:
        print("Não estamos no horário de verão!")
    elif(obj[8] == 1):
        print("Estamos no horário de verão!")
    

impressao()