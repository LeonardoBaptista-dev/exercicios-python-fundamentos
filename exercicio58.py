from random import randint  
computador = randint(0,10 )
print('Sou seu computador... Acabei de pensar em um numero entre 0 e 10.')
print('Sera que você consegue acertar qual foi? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...tente novamente...')
        elif jogador > computador:
            print('Menor, tente novamente...')
print(f'Acertou, e precisou de {palpite} tentativas.')

