import datetime

def calc_diff():
    today = datetime.date.today() #marcação do dia de hoje


    anteOntem = today - datetime.timedelta(days=2) #marcação de antes de ontem
    depoisAmanha = today + datetime.timedelta(days=2) #marcação de depois de amanha

    print("A diferençã entre antes de ontem e depois de amanhã é: ", depoisAmanha - anteOntem)

calc_diff()
