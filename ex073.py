times = ('São Paulo', 'América-MG','Atlético-GO', 'Atlético-MG', 'Avaí',
         'Botafogo', 'Bragantino', 'Ceará', 'Corinthians', 'Coritiba', 'Cuiabá',
         'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Juventude',
         'Internacional', 'Palmeiras', 'Santos')
print('=-' * 50)
print(f'Lista de times do Brasileirão: {times} ')
print('=-' * 50)
print(f'Os 5 primeiros são {times[0 :5]}')
print('=-' * 50)
print(f'Os 4 últimos são {times[-4:]}')
print('=-' * 50)
print(f'Times em ordem alfabética: {sorted(times)}')
print('=-' * 50)
print(f'O Ceará está na {times.index("Ceará")+1}ª posição')