n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('É um prazer te conhecer! {}'.format(n))
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))
