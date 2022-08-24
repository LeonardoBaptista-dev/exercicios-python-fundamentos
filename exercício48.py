soma = 0
cont = 0
for c in range(1,501,2):
    if c % 3==0:
        cont = cont + 1  #  -  todos os numeros impares multiplos de 3 de 1 a 500
    #cont = cont + 1  -  todos os numeros impares de 1 a 500
        soma = soma + c
print(f"A soma de todos os {cont} valores solicitados é {soma}")