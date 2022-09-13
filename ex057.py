sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos, digite novamente: ')).strip().upper()[0]
print('Dados inseridos com sucesso!!!'.format(sexo))
