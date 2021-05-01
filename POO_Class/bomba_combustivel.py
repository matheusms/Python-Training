class BombaCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = float(valorLitro)
        self.quantidadeCombustivel = float(quantidadeCombustivel)

    def abastecerPorValor(self, valor):
        val = valor / self.valorLitro
        print("Valor: R$ ", valor)
        print(f"Litros total: {val: .2f} L")
        self.quantidadeCombustivel -= (valor / self.valorLitro) #diminui a quantidade total sempre que abastece

    def abastecerPorLitro(self, valor):
        val = self.valorLitro * valor
        print("Litros: %d L" %valor)
        print(f"Valor a ser pago: R$ {val: .2f}")
        self.quantidadeCombustivel -= valor #diminui a quantidade total sempre que abastece
        
    def alteraValor(self, valor):
        self.valorLitro = float(valor)

    def alteraCombustivel(self, combustivel):
        self.tipoCombustivel = combustivel

    def alterarQuantidadeCombustivel(self, qtd):
        self.quantidadeCombustivel = qtd

def opções():
    print('\n')
    print(' __________________________________________________')
    print('|                                                  |')
    print("| 1 - abastecer por valor                          |")
    print("| 2 - abastecer por litro                          |")
    print("| 3 - alterar valor do Litro                       |")
    print("| 4 - alterar tipo do combustível                  |")
    print("| 5 - alterar quantidade de combustível da bomba   |")
    print("| F - Finalizar                                    |")
    print('|__________________________________________________|')
    print('\n')

def main():
    tipo = input("Tipo de combustível: ")
    preço = float(input("Preço por Litro: R$ "))
    qtdBomba = float(input("Quantidade de Litros de combustível na bomba: "))
    car = BombaCombustivel(tipo, preço, qtdBomba)
    x = True
    opções()
    while x == True:
        entrada = input("Escolha uma opção: ")
        if entrada == "1":
            val = float(input("Valor que deseja abastecer: "))
            car.abastecerPorValor(val)
        elif entrada == "2":
            Lit = float(input("Quantidade que deseja abastecer: "))
            car.abastecerPorLitro(Lit)
        elif entrada == "3":
            alt = float(input("Novo valor do litro: R$ "))
            car.alteraValor(alt)
        elif entrada == "4":
            comb = input("Selecione o tipo do combustível: ")
            car.alteraCombustivel(comb)
        elif entrada == "5":
            bomb = float(input("Quantidade de combustível na bomba: "))
            car.alterarQuantidadeCombustivel(bomb)
        elif entrada.upper() == "F":
            x = False
        else: 
            entrada = input("entrada invalida, tende novamente: ")



main()