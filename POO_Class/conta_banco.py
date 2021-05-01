#conta corrente

class Conta:
    def __init__(self, keynum, nome, correntista):
        self.key = keynum
        self.correntista = correntista
        self.nome = nome
        self.extrato=[]
        self.saldo = float(1000)#saldo inicial diferente de zero apenas para testes
        self.saldo2 = self.saldo

    def saque(self, valor):
        if (valor<self.saldo):
            self.saldo -= valor
            self.extrato.append('-> saque de R$ %d' %valor )
            return valor
        else: 
            print("Saldo insuficiente")

    def deposito(self, valor):
        self.saldo += valor
        self.extrato.append('-> depósito de R$ %d' %valor )

    def imprime_extrato(self):
        print('\n')
        print("---------- EXTRATO ----------")
        print("Conta: %d" %self.key)
        print("Nome: ", self.nome)
        if self.saldo != self.saldo2:
            print(self.extrato[0])
        print("Saldo atual: R$ %d" %self.saldo)
        print('-----------------------------')
        print("Correntista: ", self.correntista)
        print("\n")

    def alteraNome(self, newNome):
        self.nome = newNome

def opcoes():
    print('\n')
    print(' __________________________________')
    print('|                                  |')
    print("| S - para saque                   |")
    print("| D - para Depósito                |")
    print("| N - para alterar nome            |")
    print("| E - para Visualizar o Extrato    |")
    print("| F - Finalizar                    |")
    print('|__________________________________|')
    print('\n')

def main():
    nome = input("Nome: ")
    chave = int(input("Conta: (4 dígitos) "))
    corret = input("Correntista: ")
    cliente = Conta(chave, nome, corret)
    x='c'
    opcoes()
    while x.upper() != 'F':
        
        y = input("O que deseja? ")
        if y.upper() == 'S':
            sacar = float(input("valor que deseja sacar: R$ "))
            cliente.saque(sacar)
        elif y.upper() == 'D':
            dep = float(input("valor que deseja depositar: R$ "))
            cliente.deposito(dep)

        elif y.upper() == 'N':
            newNome = input("Novo nome: ")
            cliente.alteraNome(newNome)
        
        elif y.upper() == 'E':
            cliente.imprime_extrato()
        
        else:
            break
            
main()

