#inicializando uma thread com função utilizando o modulo time para aplicar um delay
from threading import Thread
import time

def func1(): #função 1 para fazer algo de exemplo
    for x in range(1,11):
        print("Processo 1 - Tarefa ", x)
        x+=1
        time.sleep(2)
    
def func2(): #função 2 para fazer algo de exemplo
    for x in range(1,11):
        print("Processo 2 - Tarefa ", x)
        x+=1
        time.sleep(1)

t1 = Thread(target=func1).start() 
t2 = Thread(target=func2).start()

#sleep permite ver a tarefa paralela de forma mais visual
