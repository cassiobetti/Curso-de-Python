import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'O preço com 10% de aumento é {moeda.aumentar(p, 10)}')
print(f'O preço com 10% de desconto é {moeda.diminuir(p, 10)}')
