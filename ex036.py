casa = float(input('Digite o valor da casa R$ '))
salario = float(input('Digite o seu salário R$ '))
anos = int(input('Digite em quantos anos você quer pagar. '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print(' A prestacão será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('EMPRESTIMO APROVADO!')
else:
    print('EMPRESTIMO NEGADO')
print('Obrigado!')