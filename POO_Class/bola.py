class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor=cor
        self.circunferencia=circunferencia
        self.material=material

    def trocaCor(self, newCor):
        self.cor=newCor

    def mostraCor(self,cor):
        print(self.cor)

#conferindo se está funcionando
a = Bola('azul', '3', 'plastico')
print("a cor é: ", a.cor)

#trocando a cor
a.trocaCor('vermelho')
print("nova cor é: ", a.cor)
