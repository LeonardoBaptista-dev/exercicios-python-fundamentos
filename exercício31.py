distancia = float(input('Qual será a distância da viagem em km?'))
if distancia <= 200:
    preço = distancia * 0.5
else:
    preço = distancia * 0.45
print('Boa viagem o preço da passagem será de R${:.2f}'.format(preço))