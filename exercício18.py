'''import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
co = math.cos(math.radians(ângulo))
tangente = math.tan(math.radians(ângulo))
print('O valor do seno, cosseno e tangente do ângulo {} é respectivamente, {:.2f}, {:.2f} e {:.2f}.'.format(ângulo, seno, co, tangente))'''

from math import radians, sin, cos, tan

ângulo = float(input('Digite um ângulo que você deseja: '))
seno = sin(radians(ângulo))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ângulo,cosseno))
tangente = tan(radians(ângulo))
print('O ângulo {} tem a TANGENTE de {:.2f} '.format(ângulo,tangente))
