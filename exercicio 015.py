dias = int(input('Quantos dias você ficou com o carro?'))
km = float(input('Quantos quilometros você percorreu com o carro?'))
dinheiro = dias * 60 + km * 0.15
print('Você irá pagar R${:.2f}'.format(dinheiro))