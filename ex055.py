maior = 0
menor = 0
for pess in range(1, 6):
    peso = float(input('Peso {}° pessoa: '.format(pess)))
    if pess == 1:
         maior = peso
         menor = peso
    else:
        if peso > maior:
            maior = peso
            if peso < menor:
                menor = peso
print('O maior peso lido foi {:.2f} Kg.'.format(peso))
print('O menor peso lido foi {:.2f} kg.'.format(peso))
