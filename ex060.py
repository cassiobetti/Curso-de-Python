from math import factorial
numero = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(numero)
print('O fatorial de {} é {}.'.format(numero, f))


# Outra forma de fazer!!!!!

numero = int(input('Digite um número para calcular seu Fatorial: '))
c = numero
f = 1
print('Calculando {}! = '.format(numero), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}.'.format(f))
