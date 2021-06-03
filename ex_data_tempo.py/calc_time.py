import time
from time import perf_counter

#imprimir com delay de 3 segundos 5 vezes

def delayTime(): 
    for i in range(5):
        time.sleep(3)
        print("Olá mundo")
    
    



start_time = time.time()#tempo inicial de execução atraves do time.time()
start_counter = perf_counter()#tempo inicial de execução atraves do perf_counter()
delayTime()
end_time = time.time()#tempo final de execução atraves do time.time()
end_counter = perf_counter()#tempo final de execução atraves do perf_counter()
print("O tempo de execução time.time(): ", end_time - start_time)
print("tempo de exe Perf_counter: ", end_counter - start_counter)