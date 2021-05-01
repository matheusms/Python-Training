global FL

def cria_fila():
    global FL
    FL=[]

def insere():
    global FL
    x = int(input("Inserir o número: "))
    FL.append(x)

def fila_vazia(f):
    return len(f)==0

def obter_frente(f):
    if not fila_vazia(f):
        print(f[0])
    else:
        print('Fila Vazia!')

def obter_fim(f):
    if not fila_vazia(f):
        print(f[-1])
    else:
        print('Fila Vazia!')

def remove(f):
    if not fila_vazia(f):
        aux = f[0]
        del f[0]
        return aux
    else:
        print('Fila Vazia!')

def mostrar_fila(f):
    if not fila_vazia(f):
        print('Inicio ->', end=' ')
        for i in range(len(f)):
            print(f[i], end=' ')
        print('<- Fim')
    else:
        print('Fila Vazia!')

def opcao():
    print('Inserir(I)')
    print('Obter o primeiro da fila(P)')
    print('Obter o último da fila(U)')
    print('Mostrar Fila(M)')
    print('Remover o 1º(R)')
    print('Fim(F)')
    print("                         -> Atenção <-                            ")
    print("->Para se iniciar outra fila deve-se abrir o programa novamente!<-")


def main():
    opcao()
    cria_fila()#criando apenas 1 vez, se nao zera tudo
    p='s'
    while p=='s':
        z=input("Selecione uma opção: ")            
        if (z.upper() == 'I'):
            insere()
        elif (z.upper() == 'P'):
            obter_frente(FL)#retorna o valor zero da fila, no caso o primeiro
        elif (z.upper() == 'M'):
            mostrar_fila(FL)
        elif (z.upper() == 'U'):
            obter_fim(FL)
        elif (z.upper() == 'R'):
            remove(FL)#remove o primeiro da fila
        elif (z.upper() == "F"):
            p = z
        else:
            print("Opção inválida, tente novamente!")
    print("O programa Acabou! Tenha ótimo dia!")
          
main()
