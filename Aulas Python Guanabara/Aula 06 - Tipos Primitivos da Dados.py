# Função (.format) faz com que se aloque varios valores em sequencia dentro de uma string sem precisar colocar varias
# vírgulas e aspas
# Para mostrar apenas duas casa decimais usa-se dentro das chaves {:.2f} faz com que um número mostre
# apenas duas casas depois da virgula ou ponto no caso do padrao americano

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite mais um numero: '))
s = n1+n2
print('A soma de {} + {} é igual a {}'.format(n1, n2, s))