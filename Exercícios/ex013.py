# Faça um algoritmo que leia o salario de um funcionario e mostre o seu novo salario, com 15% de aumento.

sal = float(input('Qual o seu salário? R$'))
aum = sal + (sal * 15 / 100)
print('Seu salário passou a ser R${:.2f}'.format(aum))