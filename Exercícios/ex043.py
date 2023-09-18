# Desenvolva uma lógia que leia o peso e a altura de uma pessoa.
# calcule o seu IMC e mostre seu status de acordo com a tablea abaixo

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / (altura ** 2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))

