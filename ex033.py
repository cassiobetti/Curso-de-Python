a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo numero: '))
c = int(input('Digite o terceiro número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor número é {}'.format(menor))
print('O maior número é {}'.format(maior))
