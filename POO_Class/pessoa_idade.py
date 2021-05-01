class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.altura=altura


    def envelhecer(self, newIdade):
        if (self.idade<21) and (newIdade > self.idade):
            for i in range(newIdade - self.idade):
#adiciona 5 cm na altura para ter a altura estimada a cada ano
                self.altura_idade=self.altura+0.05
            print(f'nova altura de acordo com idade: {self.altura_idade:.2f} m')

#verifica se engordou
    def engordar(self, newPeso):
        if newPeso > self.peso:
            engordou = newPeso - self.peso
            self.peso=newPeso
            print("engordou: ", engordou, "Kg")

#verifica se emagreceu
    def emagrecer(self, newPeso):
        if newPeso<self.peso:           
            emagreceu = self.peso - newPeso
            self.peso=newPeso
            print("emagreceu: ", emagreceu, "Kg")

#verifica se cresceu
    def crescer(self, newAltura):
        if newAltura>self.altura:
            cresceu = newAltura - self.altura
            self.altura=newAltura
            print(f"cresceu: {cresceu: .2f} m")

def calcular(Pessoa):
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    peso = int(input("Peso: "))
    altura = float(input("Altura: (metros)"))
    p = Pessoa(nome, idade, peso, altura)
    x=0
    #chama de novo para checar as novas medidas a partir da idade
    print('---------*Novas medidas*---------')
    newIdade = int(input("Idade: "))
    newPeso = int(input("Peso: "))
    newAltura = float(input("Altura: (metros)"))
    p.emagrecer(newPeso)
    p.engordar(newPeso)
    p.envelhecer(newIdade)
    p.crescer(newAltura)


def main():
    calcular(Pessoa)
    
main()
