#tempo em segundos que se passaram desde uma epoca 
import time

def segundos_inicio():
    seconds = time.time()

    print("Segundos desde a época: ", seconds)

    #imprime no tempo atual
    local_time = time.ctime(seconds)
    print("Tempo atual: ", local_time)

    #tempo no momento atual
    print("Tempo local: ", time.asctime())

    #imprime dados do tempo derivados do sintaxe de struct
    print(time.localtime())

    #cria um objeto localtime e imprime o valor na posição desejada
    a = time.localtime()
    print("Ano: ", a[0]) #imprime o ano
    print(a[3:6])#hora, min, seg

    #editando como vou imprimir o localtime()
    a = time.strftime("%Y-%m-%d-%H.%M.%S", time.localtime())
    print(a)

segundos_inicio()