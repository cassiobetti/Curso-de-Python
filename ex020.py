import random
a = input('Digite o nome do aluno 1: ')
b = input('Digite o nome do aluno 2: ')
c = input('Digite o nome do aluno 3: ')
d = input('Digite o nome do aluno 4: ')
lista = [a, b, c, d]
random.shuffle(lista)

print('A ordem de apresentação será ')
print(lista)
