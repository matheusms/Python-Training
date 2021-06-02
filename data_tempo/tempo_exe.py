import time

start_exec = time.time()#cria um marco de tempo para a contagem

def hello():
    time.sleep(5)
    print("teste de contagem 5 segundos")

hello()
end_exec = time.time() #marcação final do processamento
print("O tempo de execução é: ", end_exec - start_exec)