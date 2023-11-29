# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou do tempo de alistamento
# Seu programa tambpem deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
atual = date.today().year
ano = int(input('Em que ano você nasceu? '))
id = atual - ano
print('Quem nasceu em {} tem {} em {}.' .format(ano, id, atual))
if id > 18:
    passou = id - 18
    print('Você ja ultrapassou a idade para o alistamento militar em {} anos.'.format(passou))
elif id < 18:
    falta = 18 - id
    print('Você ainda não atingiu a data para se alistar ao serviço militar, ainda lhe resta {} anos.'.format(falta))
else:
    print('Está na hora de se alistar ao serviço militar, digira-se ao posto mais próximo!')
