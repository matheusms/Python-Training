from time import perf_counter

#entrando com dois numeros inteiros a partir do usuário
print("Entre com dois valores inteiros: ")
n = int(input())
m = int(input())

#marcador de tempo inicial
t1_start = perf_counter()

for i in range(n):
    t = int(input("Insira um valor inteiro: "))
    #dando entrada de um valor n vezes

    if t % m == 0:
        print(t)

#marcador de tempo final
t1_stop = perf_counter()

print("Tempo de duração: ", t1_stop, t1_start)
print("tempo decorrido durante todo o programa, em segundos: ", t1_stop-t1_start)