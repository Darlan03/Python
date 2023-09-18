# Desenvolva um programa que leia as notas de um aluno, calcule e mostre a sua média.

n1 = float(input('Digite sua nota no primeiro semestre: '))
n2 = float(input('Digite sua nota no segundo semestre: '))
m = (n1+n2)/2
print('A sua média é {:.1f} '.format(m))
if (m) >= 7:
    print('Parabéns, você foi aprovado!')
else:
    print('Não foi dessa vez :( mas não desista!')