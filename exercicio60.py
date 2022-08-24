#usando módulo

'''from math import factorial

n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n}, é {f}.')'''

#fazendo manualmente

n = int(input('Digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'Calculando fatorial de {n}...')

#while c > 0:

for c in range(c,0,-1):
    print(f'{c}', end='')
    if c > 1:
        print(' x ', end='')  
    else:
        print(' = ', end='')
    f *= c
      
print(f'{f}')
