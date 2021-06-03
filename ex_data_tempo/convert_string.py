from datetime import datetime


def convert_string():
    texto = '01 de janeiro de 2021 13h53'
    texto2 = texto.split(' ')

    #dicionario para tratar com o nome do mês
    meses = {'janeiro': '01', 'fevereiro': '02', 'março': '03', 'abril': '04', 'maio': '05', 'junho': '06', 'julho': '07', 'agosto': '08', 'setembro': '09', 'outubro': '10', 'novembro': '11', 'dezembro': '12'}
    trat_hora = texto2[5].split('h')
    #concatenando
    data = texto2[4] + '-' + meses[texto2[2]] + '-' + texto2[0] + '-' + trat_hora[0] + '-' + trat_hora[1] + '-' + '00'

    
    final = datetime.strptime(data, '%Y-%m-%d-%H-%M-%S')
  
    print(final)
    

convert_string()