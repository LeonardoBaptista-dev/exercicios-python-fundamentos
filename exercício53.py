frase = str(input("Digite uma frase: ")).strip().upper() # tirar os espaços e transformar tudo em maiusculas
palavras = frase.split() # Separar a frase em uma lista ex= ["O","Livro","é","bom"]
junto = ''.join(palavras) # Juntar a lista sem espaço.
inverso = junto[::-1] # inverte usando fatiamento mais  simples
#for letra in range(len(junto)-1, -1, -1): # processo para inverter frase usando for, converter em lista
#    inverso += junto[letra] # juntar as partes ao contrario
print('O inverso de {} é {}'.format(junto,inverso))
if junto == inverso:
    print("Sim essa frase é um palindromo, desconsiderando os espaços.")
else:
    print('Não esta frase não é um palindromo')
         