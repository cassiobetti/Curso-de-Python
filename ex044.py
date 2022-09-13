print('{:=^40}'.format(' LOJAS BETTI '))
preço = float(input('Digite o valor das compras: R$ '))
print('''FORMAS DE PAGAMENTOS
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('DIGITE A OPÇÃO: '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x SEM JUROS de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada e, {}x de  R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('OPÇÃO INVALIDA')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
