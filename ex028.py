from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar.')
print('-=-' * 20)
jogador = int(input('Digite o número escolhido pelo computador entre 0 e 5: '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('Você acertou!')
else:
    print('Você errou!')
print('O número escolhido pelo computador foi? {}'.format(computador))
