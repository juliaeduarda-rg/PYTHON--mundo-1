n1 = int(input('digite um numero:'))
n2 = int(input('digite outro numero:'))
s = n1+n2
print('a soma entre {} e {} é igual a {}'.format(n1, n2, s))

n = input('escreva algo')
print('O valor desse caractere é:', type(n))
print('É um número?', n.isnumeric())
print('Só tem espaços?', n.isspace())
print('Está em maiusculo?', n.isupper())
print('Está em minusculo?', n.islower())
print('São letras?', n.isalpha())