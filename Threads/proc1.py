from threading import Thread
import threading

def proc1():
    print("Processo 1")

t1 = Thread(target=proc1).start()
print("Ativo: ", threading.currentThread().is_alive()) #verificando se esta ativo
print("Nome: ", threading.currentThread().getName()) #nome da thread
print("Identificador de Thread: ", threading.get_ident()) #identificador da thread
print("Qtd de Threads ativas: ", threading.active_count())
print("Threads ativas: ", threading.enumerate())