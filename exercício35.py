print('-='*50)
print('Digite três seguimentos para que o programa cálcule se é possível formar um triângulo ou não.')
print('-='*50)
r1 = float(input('Primeiro seguimento: '))
r2 = float(input('Segundo seguimento: '))
r3 = float(input('Terceiro seguimento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print('Com esses três segmentos é possível formar um triângulo.')
else:
    print('Com esse três segmentos não é possível formar um triângulo.')