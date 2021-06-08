import random
a1 = input('primeiro aluno:')
a2 = input('segundo aluno: ')
a3 = input('terceiro aluno: ')
a4 = input('quarto aluno: ')
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(lista)