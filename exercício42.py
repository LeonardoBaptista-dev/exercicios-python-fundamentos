print('-='*60)
print('Digite 3 segmentos para que o programa calcule sé e possivel formar um triangulo e se sim qual o tipo de triangulo')
print('-='*60)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar um triangulo.')
    if r1 == r2 and r2 == r3:
        print('E ele é Equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('E ele é um triangulo Isóceles.')
    elif r1 != r2 != r3 != r1:
        print('E ele é um triangulo Escaleno. ')
else:
    print('Os segmentos não podem formar um triangulo.')
print('-='*60)
