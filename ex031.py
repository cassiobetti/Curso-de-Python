d = float(input('Digite a distância da viagem em Km: '))
print('A distância da viagem foi de {} km'.format(d))

if d <= 200:
    m = d * 0.50
else:
    m = d * 0.45
print('O valor da passagem é de: R${:.2f}'.format(m))
