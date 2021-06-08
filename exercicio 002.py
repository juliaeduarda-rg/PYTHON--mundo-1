n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
su = n1 - n2
di = n1 // n2
p = n1 ** n2
print('A soma é: {} a subtração é: {}, a multiplicação é: {}, e a divisão é: {:.2f}'.format(s, su, m, d), end=' ')
print('A divisão inteira é: {} e a potência: {}'.format(di, p))
