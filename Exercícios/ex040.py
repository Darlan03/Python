# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com
# a media atingida
# Media abaixo de 5.0: reprovado
# Meida entre 5.0 e 6.9: recuperação
# Media 7.0 ou superior: Aprovado

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('Sua media é {}'.format(media))
if media < 5:
    print('Você não atingiu a media necessária, você foi reprovado!')
elif media < 7:
    print('Você não atingiu a media necessária, você está de recuperação!')
else:
    print('Parabéns, você foi aprovado!')
