ips = []
lista_validos = ['200.135.80.9', '192.168.1.1', '8.35.67.75', '1.2.3.4']
lista_invalidos = ['257.32.4.5', '85.345.1.2', '9.8.234.6', '192.168.0.256']
ip_val = []
ip_inv = []

def leitura():
    arq = open('ip.txt', 'r')
    texto = arq.readlines() 
    arq.close()
    for i in texto:
        a1 = i.split('\n') #pegando linha por linha
        a2 = a1[0].split(' ') #reduzindo para facilitar de trabalhar
        t = a2[0] #ip salvo 
        ips.append(t)#salvando tudo em uma lista
    #print(ips[0])

def validar(): #verificando validade dos ip's e escrevendo como txt
    
    ip_val.append('[Endereços válidos:]')
    ip_inv.append('[Endereços inválidos:]')

    for i in ips:
        if i in lista_validos: #verifica se é um ip valido e salva na lista de validos
            ip_val.append(i)
            
        elif i in lista_invalidos: #salva os arquivos em uma lista de ip invalidos
            ip_inv.append(i)

def imprimir():
    for i in ip_val:
        print(i)
    print('\n')

    for i in ip_inv:
        print(i)


def main():
    leitura()
    validar()
    imprimir()

main()
