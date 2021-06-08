v = float(input('Diga a velocidade do carro:'))
if v >= 80:
    print('Você foi mutado meu chapa. R${:.2f}'.format((v - 80) * 7))
else:
    print('Tudo certo.')