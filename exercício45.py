from random import randint
itens = ("Pedra", "Papel","Tesoura")
computador = randint(0,2)
print("""Suas opções: 
[0] PEDRA
[1] PAPEL
[2] TESOURA""")
jogador = int(input('Qual é a sua jogada: '))
print("-=" *20)
print(f"Computador jogou {itens[computador]}")
print(f"O Jogador jogou {itens[jogador]}")
print("-="*20)
if computador == 0: # computador jogou pedra
    if jogador == 0:
        print("Empate jogue novamente")
    elif jogador == 1:
        print("O jogador ganhou.")
    elif jogador == 2:
        print("Computador ganhou.")
elif computador == 1:
    if jogador == 0:
        print("Computador ganhou.")
    elif jogador == 1:
        print("Deu empate.")
    elif jogador == 2:
        print("Jogador ganhou")
elif computador == 2:
    if jogador == 0:
        print("Jogador ganhou.")
    elif jogador == 1:
        print("Computador ganhou.")
    elif jogador == 2:
        print("Deu empate.")
print("-="*20)
   
    


