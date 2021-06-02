#criando delay de tempo: atrasa a exe. do thread atual por determinado n° de segundos
import time

def delay_1():
    print("teste de impressão imediato")
    time.sleep(5)#sleep for 5 seconds
    print("teste de impressão após 5 segundos")

