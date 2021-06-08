nome = str(input('Nome completo:')).strip()
nome = nome.split()
print('primeiro nome:{}'.format(nome[0]))
print('ultimo nome:{}'.format(nome[len(nome)-1]))