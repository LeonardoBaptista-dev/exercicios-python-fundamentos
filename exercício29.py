'''Ler a velocidade do carro'''
velocidade = float(input('Qual a velocidade do veículo?'))
if velocidade > 80:
    print('Multado! Você execeu o limite permitido que é de 80km/h.')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}.'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')

