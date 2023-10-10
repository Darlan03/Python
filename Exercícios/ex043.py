# Desenvolva uma lógia que leia o peso e a altura de uma pessoa.
# calcule o seu IMC e mostre seu status de acordo com a tablea abaixo

peso = float(input('Qual é seu peso (Kg)? '))
altura = float(input('Qual é sua altura (m)? '))
imc = peso / (altura ** 2)
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso!\nProcure ajuda médica!')
elif imc < 24.9:
    print('Você está com peso adequado, parabéns!')
elif imc == 25 or imc < 29.9:
    print('Você está com sobrepeso, cuidado!')
elif imc == 30 or imc < 34.9:
    print('Você está com obesidade grau 1, cuidado!')
elif imc == 35 or imc < 39.9:
    print('Você está com obesidade grau 2 (severa)!\nProcure ajuda médica!')
elif imc > 40:
    print('Você está com obesidade obesidade grau 3 (mórbida))!\nProcure ajuda médica!')
