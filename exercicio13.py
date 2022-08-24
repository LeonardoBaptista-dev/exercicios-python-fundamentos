sal = float(input('Qual o salário atual do funcionário? R$ '))
novo = sal + (sal*15/100)
print('O salário do funcionário de R${:.2f}, com 15% de aumento passa a receber R${:.2f}.'.format(sal,novo))
