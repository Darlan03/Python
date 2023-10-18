# Faça um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais o aumento é de 15%.

print('-=-' * 8)
print('AUMENTO DE SALÁRIO!!!')
print('-=-' * 8)
sal = float(input('Qual o seu salário atual? '))
if sal > 1250:
    aum = sal + (sal * 10)/100
else:
    aum = sal + (sal * 15)/100
print('Parabéns, seu novo salário passou a ser R${:.2f}'.format(aum))