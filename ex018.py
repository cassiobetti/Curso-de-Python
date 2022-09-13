import math
a = float(input('Digite o ângulo: '))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('O ângulo é de: {:.2f}, o seno é: {:.2f}, o cosseno é: {:.2f}, a tangente é: {:.2f}'.format(a, s, c, t))
