# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))
d = n*2
t = n*3
r = n**0.5
print('O dobro de {} é {}. '.format(n, d))
print('O triplo é {} é {}. \nA raiz quadrada de {} é {:.2f}. '.format(n, t, n, r))


print('O dobro é {}. \nO triplo é {}. \nA raiz quadrada é {:.2f}. '.format((n*2), (n*3), (pow(n,(1/2)))))
