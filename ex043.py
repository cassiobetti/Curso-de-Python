peso = float(input('Digite o seu peso: (Kg)'))
altura = float(input('Digite a sua altura: (m)'))
imc = peso / (altura ** 2)
print('O imc dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')