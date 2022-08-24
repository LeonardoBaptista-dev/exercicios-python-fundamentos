
casa = float(input('Qual o valor da casa: R$')) # perguntar valor da casa
salario = float(input('Qual o valor do salário: R$')) # perguntar salário do comprador
anos = int(input('Em quantos anos vai pagar o financiamento? '))# quantos anos vai pagar
prestação = casa /(anos * 12)
minimo = salario * 30 /100
# Calcular o valor da prestação mensal, não pode exceder o 30% do sálario, senão negar empréstimo
if prestação <= minimo:
    print('Seu financiamento foi aprovado, sua prestação mensal ficou em R$ {:.2f}.'.format(prestação))
else:
    print('Infelizmente seu financiamento não foi aprovado.')

