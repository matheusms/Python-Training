#escrever primeira letra do nome com letra maiúscula
nome= input("Digite seu nome: ")
nome=nome.lower()
L=nome.strip()
L=nome.split()



aux = ''
for n in L:
    
    L = n[0:1].upper()+n[1::]
    #print(n)
    aux = aux + ' ' + L 

print (aux.strip())
    
    
