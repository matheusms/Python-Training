class Quadrado:
    def __init__(self, lado):
        self.lado=lado


    def mudaLado(self, newLado):
        self.lado=newLado

    def imprimeLado(self):
        print(self.lado)

    def area(self):
        return self.lado * self.lado

#definindo o quadrado
q = Quadrado(2)
#imprimir o lado do quadrado
q.imprimeLado()
#imprimindo a area do quadrado
print(q.area())
#trocando o lado do quadrado
q.mudaLado(3)
#imprimindo o novo lado
q.imprimeLado()
