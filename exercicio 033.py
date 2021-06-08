num1 = int(input('escreva um numero:'))
num2 = int(input('escreva um numero:'))
num3 = int(input('escreva um numero:'))
menor = num1
if num2<num1 and num2<num3:
    menor = num2
if num3<num1 and num3<num2:
    menor = num3
maior= num1
if num2>num1 and num2>num3:
    maior = num2
if num3>num1 and num3>num2:
    maior = num3
print('Entre {}, {} e {}. O menor número é {} e, o maior número é {}'.format(num1, num2, num3, menor, maior))