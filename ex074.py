from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Eu sorteei os valores {n}')
print(f'O menor número sorteado foi {min(n)}')
print(f'O maior número sorteado foi {max(n)}')
