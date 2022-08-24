#criar um programa que perg o salario de um funcionario e calcule o valor do seu aumento
#para salarios superiores a 1.250,00 calcule aumento de 10%
#para salarios inf ou iguais o aumento é de 15%.

salario = float(input('Qual o valor do salário do funcionário?  '))
if salario <= 1250:
    novo = (salario * 0.15) + salario
else:
    novo = (salario * 0.10) + salario
print('O novo valor do salário com aumento será de R${:.2f}.'.format(novo))
