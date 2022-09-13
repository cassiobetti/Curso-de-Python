from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de seu nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))
if idade < 18:
    saldo = 18 - idade
    print('Você ainda vai se alistar, faltam {}ano(s) para o seu alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))
elif idade == 18:
    print('Chegou a hora de você se alistar! ')
else:
    saldo = idade - 18
    print('Já passou {} ano(s) do seu alistamento.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))

