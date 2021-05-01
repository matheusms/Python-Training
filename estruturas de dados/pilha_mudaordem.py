from collections import deque

def A_pilha(self):
    aux=[]
    pilha=[]
    seqA=''
    for c in self:
        if (c.isalpha() is True):
            pilha.append(c)
        else:
            aux.append(c)

    for i in range(len(aux)):   
        pilha.append(aux.pop())

    for j in pilha:#apenas por questão de impressão
        seqA+=j

    print(self, '---->', seqA)


def A_fila(self):
    fila=deque()
    aux=deque()
    seqA=''
    for c in self:
        if (c.isalpha() is True):
            fila.append(c)
        else:
            aux.append(c)
    aux.reverse()

    for i in aux:
        fila.append(i)

    for j in fila:#apenas por questão de impressão
        seqA+=j
    print(self, '---->', seqA)


def ehDigito(self):
    for i in self:
        print(type(i))

def main():
    seq = 'A1E5T7W8G'
    #letra A por pilha
    A_pilha(seq)
    #letra A por filas
    A_fila(seq)
    """acho que acabei resolvendo as filas e pilhas como metodo da letra b, e a
    letra a seria feita usando for intercalando par e impar para cada um."""
    

main()


