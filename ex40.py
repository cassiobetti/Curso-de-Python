n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('REPROVADO')
elif m >= 5 or m <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
print('Obrigado!')
