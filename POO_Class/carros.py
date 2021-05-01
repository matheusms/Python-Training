class Carro:
    def __init__(self, cor, marca, modelo):
        self.cor=cor
        self.marca=marca
        self.modelo=modelo

    def mudaCor(self, newCor):
        self.cor=newCor

    def imprimeDados(self):
        print("cor: ", self.cor, ", marca: ", self.marca, ", modelo: ", self.modelo)

    def setModelo(self, newModelo):
        self.modelo=newModelo


#metodo rapido para rodar 3 vezes e salvar cada carro
for i in range (3):
    if i == 0:
        print('*--selecione os dados do carro A --*')
        cor = input('cor: ')
        marca = input('marca: ')
        modelo = input('modelo: (Sedan, Hatch, Sport)')
        carroA=Carro(cor, marca, modelo)
    elif i == 1:
        print('*--selecione os dados do carro B --*')
        cor = input('cor: ')
        marca = input('marca: ')
        modelo = input('modelo: (Sedan, Hatch, Sport)')
        carroB=Carro(cor, marca, modelo)
    else:
        
        print('*--selecione os dados do carro C --*')
        cor = input('cor: ')
        marca = input('marca: ')
        modelo = input('modelo: (Sedan, Hatch, Sport)')
        carroC=Carro(cor, marca, modelo)


#mudando a cor
car = input('qual carro deseja trocar a cor? (A, B OU C) ')
car=car.upper()
muda = input('nova cor: ')

if car == 'A':
    carroA.mudaCor(muda)
    print('nova cor carro A: ')
    carroA.imprimeDados() 

elif car == 'B':
    carroB.mudaCor(muda)
    print('nova cor carro B: ')
    carroB.imprimeDados() 

else:
    carroC.mudaCor(muda)
    print('nova cor carro C: ')
    carroC.imprimeDados() 

#mudando o modelo 
car = input('qual carro deseja trocar o modelo? (A, B OU C) ')
car=car.upper()
muda = input('novo modelo: ')

if car == 'A':
    carroA.setModelo(muda)
    print('novo modelo carro A: ')
    #carroA.imprimeDados() 

elif car == 'B':
    carroB.setModelo(muda)
    print('novo modelo carro B: ')
    #carroB.imprimeDados() 

else:
    carroC.setModelo(muda)
    print('novo modelo carro C: ')
    #carroC.imprimeDados() 

print('novos dados: ')
carroA.imprimeDados()
carroB.imprimeDados()
carroC.imprimeDados()
