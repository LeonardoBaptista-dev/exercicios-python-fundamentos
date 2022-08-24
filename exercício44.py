#programa que calcule desconto de acordo com o tipo de pagamento.

print('{:=^50}'.format('Lojas Colletti'))
print('-='*25)
print('Software para calcular descontos')
print('-='*25)
valorpago = float(input('Digite o valor a ser pago sem desconto: R$ '))
print('''
[1] à vista dinheiro/cheque: 10% de desconto
[2] à vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço normal
[4] 3x ou mais no cartão: 20% de juros 
''')
tipo = int(input('Qual o tipo de pagamento: '))
print('-='*60)

if tipo == 1:
    valor = valorpago - (valorpago *0.10)
    print('O valor a ser pago com desconto de 10% é de R${:.2f}. '.format(valor))
elif tipo == 2:
    valor = valorpago - (valorpago * 0.05)
    print('O valor a ser pago com desconto de 5% é de R${:.2f}. '.format(valor))
elif tipo == 3:
    print('O valor a ser pago é de R${:.2f}'.format(valorpago))
elif tipo == 4:
    valor = valorpago + (valorpago * 0.2)
    print('O valor total a ser pago considerando os juros do parcelamento é de R${:.2f}'.format(valor))
else:
    print('Opção inexistente, escolher umas das 4 opções disponíveis. ')