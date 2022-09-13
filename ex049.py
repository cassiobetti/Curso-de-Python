from time import sleep
num = int(input('Digite um número para ver sua tabuada: '))
print('O número digitado foi {}.'.format(num))
for n in range(0, 11):
    sleep(1)
    print('{} x {} = {}'.format(num, n, (num * n)))



