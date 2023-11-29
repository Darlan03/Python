# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
# a sua categoria, de acordo com a idade:
# Até 9 anos: mirim
# Até 14 anos: infantil
# Até 19 anos: junior
# Até 20 anos: senior
# Acima: master

from datetime import date
atual = date.today().year
ano = int(input('Em que ano você nasceu? '))
id = atual - ano
print('Quem nasceu {} tem {} anos em {}'.format(ano, id, atual))
if id <= 9:
    print('De acordo com sua idade você se enquadra na categoria Mirim.')
elif id <= 14:
    print('De acordo com sua idade você se enquadra na categoria Infantil.')
elif id <= 19:
    print('De acordo com sua idade você se enquadra na categoria Junior.')
elif id <= 25:
    print('De acordo com sua idade você se enquadra na categoria Senior.')
else:
    print('De acordo com sua idade você se enquadra na categoria Master.')