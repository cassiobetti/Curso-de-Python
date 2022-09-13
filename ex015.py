Km = float(input('Quantidade de KM percorridos: '))
Dias = float(input('Quantidade de dias de aluguel do carro: '))
cd = Dias * 60.0
ck = Km * 0.15
s= cd + ck
print('A quantidade de kilometros percorrido foi de: {}'.format(Km))
print('A quantidade de dias de aluguel do carro foi de: {}'.format(Dias))
print('O preço a pagar pelo aluguel é de: {}'.format(s))