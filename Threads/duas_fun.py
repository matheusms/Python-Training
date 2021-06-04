from threading import Thread, ThreadError
import threading
import time

def proc1():
    
    time.sleep(5)
    print("Processo 1")

def proc2():
    
    time.sleep(30)
    print("Processo 2")

t1 = Thread(target=proc1)
t2 = Thread(target=proc2)

t1.start()
t2.start()
print("Ativo: ", threading.currentThread().is_alive()) 

print("Processo 1 esta ativo: ", t1.is_alive()) #verifica se processo t1 ta ativo
print("Processo 2 esta ativo: ", t2.is_alive())#verifica se processo t2 ta ativo

t1.join()
t2.join()

print("Acabou")