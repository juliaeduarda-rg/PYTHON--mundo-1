a = float(input('Qual a altura da sua parede?'))
l = float(input('Qual a largura da sua parede?'))
r = a * l
print('A area da sua parede é {}m²'.format(r))
print('Para pinta-la inteira, vai ser necessario {}L de tinta'.format(r / 2))