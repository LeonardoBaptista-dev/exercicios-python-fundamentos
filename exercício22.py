nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome completo em letras minusculas é {}.'.format(nome.lower()))
print('Seu nome completo em letras maiúsculas é {}.'.format(nome.upper()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separado = nome.split()
print('Seu primeiro nome tem é {} e ele tem {} letras.'.format(separado[0], len(separado[0])))

