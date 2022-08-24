'''Faça um  jogo simples que faça com que o computador sorteie um numero de 0 a 5 e peça para o usuario tentar acertar qual foi o numero escolhido'''
from random import randint

numcpu = randint(0,5)  # Faz o computador "PENSAR
print('-=-'*20)
print('Vou pensar em número entre 0 e 5. Tente adivinhar...? ')
print('-=-'*20)
numjogador = int(input('Em que númeroo pensei?')) # jogador tenta adivinhar
if numcpu == numjogador:
    print('Parabéns você acertou o número sorteado!')
else:
    print('Que pena, infelizmente você não acertou o número sorteado, eu pensei no número {} e não no número {} tente novamente.'.format(numcpu,numjogador))




