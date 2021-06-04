#inicializando uma thread com função
from threading import Thread

def func1(): #função 1 para fazer algo de exemplo
    for x in range(1,11):
        print("Processo 1 - Tarefa ", x)
        x+=1
    
def func2(): #função 2 para fazer algo de exemplo
    for x in range(1,11):
        print("Processo 2 - Tarefa ", x)
        x+=1
    
t1 = Thread(target=func1).start() 
t2 = Thread(target=func2).start()
