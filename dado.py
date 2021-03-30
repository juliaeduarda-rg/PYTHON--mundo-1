from time import sleep
from random import randint
print('_-'*10)
print('Seja bem vindo!')
print('_-'*10)
sleep(1)
usuario = int(input('''Escolha o seu dado:
D3 | D4 | D6 | D8 | D10 | D12 | D20 | D100 | [0]outro 
D:'''))
if usuario == 3:
    print(randint(1, 3))
elif usuario == 4:
    print(randint(1, 4))
elif usuario == 6:
    print(randint(1, 6))
elif usuario == 8:
    print(randint(1, 8))
elif usuario == 10:
    print(randint(1, 10))
elif usuario == 12:
    print(randint(1, 12))
elif usuario == 20:
    print(randint(1, 20))
elif usuario == 100:
    print(randint(1, 100))
elif usuario == 0:
    dado = int(input('Qual o número do seu dado?'))
    print(randint(1, dado))
else:
    print('Dado invalido tente novamente.')