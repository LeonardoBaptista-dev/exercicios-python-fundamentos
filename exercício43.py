print('-='*60)
print('Digite seu peso e sua altura para que o programa calcule se você está ou não dentro do seu peso ideal.')
print('-='*60)

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura**2)
print('-='*60)
print('O resultado do seu cálculo de IMC foi {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade morbida.')
print('-='*60)
