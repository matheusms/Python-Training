class Retangulo:
    def __init__(self, base, altura):
        self.base=base
        self.altura=altura

    def mudaLado(self, newBase, newAltura):
        self.base=newBase
        self.altura=newAltura

    def imprimeLado(self):
        print("a base é: ", self.base)
        print("a altura é: ", self.altura)

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return self.base + self.altura + self.base + self.altura


def main():    
    
    #calculando a area do local
    base=int(input("base do local: "))
    altura=int(input("altura do local: "))
    ret = Retangulo(base, altura)
    ret.imprimeLado()
    print(ret.area())

    newBase=int(input('lado novo: '))
    newAltura = int(input('altura nova: '))
    ret.mudaLado(newBase, newAltura)
    ret.imprimeLado()
  
    #calculando a area do piso e quantos cabem
    base=int(input("base do piso: "))
    altura=int(input("altura do piso: "))
    piso = Retangulo(base,altura)

    #calculando quantos pisos
    n_pisos = (ret.area() / piso.area())+1 #caso seja necessário com numeros quebrados
    print('os numeros de pisos são: ', n_pisos)

    #calculando quantos rodapés
    rodape = float(input('insira o comprimento do rodapé em metros: '))
    n_rodape = (ret.perimetro())/rodape
    print('numero de rodapés é: ', n_rodape)
main()

