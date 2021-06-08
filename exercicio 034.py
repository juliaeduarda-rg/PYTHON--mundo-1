sal = float(input('Qual é o seu salario?'))
if sal >=1250.00:
    print('Seu novo salario é {:.2f}'.format(sal +(10 / 100 * sal)))
else:
    print('Seu novo salario é {:.2f}'.format(sal +(15 / 100 * sal)))