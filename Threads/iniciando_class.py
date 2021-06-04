#inicializando um thread em classe
from threading import Thread
import threading
import time

class iniThread:
    def imprime(self):
        i=0
        print(threading.current_thread().getName()) #imprimir o nome da thread current
        time.sleep(1)
        while(i<=10):
            print(i)
            i+=1
        
obj = iniThread()
t1 = Thread(target=obj.imprime)
t1.start()

t2 = Thread(target=obj.imprime)
t2.start()

t3 = Thread(target=obj.imprime)
t3.start()