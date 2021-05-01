class Televisão:
    def __init__(self):
        self.status = False
        self.canal = 2 #canal salvo de standby
        self.volume = 50 #volume padrao

    def ligar(self, status): 
        self.status = status

    def mudacanal(self, newcanal):
        self.canal = newcanal
        print('Novo canal: ', self.canal)

    def aumentVolume(self):
        aux = self.volume + 10
        if aux <= 100:
            self.volume+=10
            print('volume: ', self.volume)
        else:
            self.volume = 100
            print('volume máximo 100')
        
    def diminuiVolume(self):
        axu = self.volume - 10
        if axu >= 0:
            self.volume-=10
        else: 
            self.volume = 0
            print('volume mínimo 0')



def main():
    tv = Televisão()
    ligar = input("Deseja ligar a TV? (S/N)")
    if ligar.upper() == "S":
        t = True
        tv.ligar(t)
    
    canal = int(input("Digite um canal: "))
    tv.mudacanal(canal)

    vol = input("(+) - aumentar volume | (-) - diminuir volume: ")
    if vol == "+":
        tv.aumentVolume()
    
    elif vol == "-":
        tv.diminuiVolume()
main()



        