real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dol = real / 3.27
print('Com R${:.2f} que você tem na carteira é possível comprar US${:.2f}.'.format(real, dol))
