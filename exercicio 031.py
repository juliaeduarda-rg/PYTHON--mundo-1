dist = int(input('Qual a distancia da viagem?'))
if dist <= 200:
    print('O valor da passagem é R${}'.format(0.50 * dist))
else:
    print('O valor da pasagem é R${}'.format(0.45 * dist))