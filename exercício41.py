from datetime import date
atual = date.today().year
nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = atual - nascimento
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Com essa idade, o atleta se enquadra na categoria Mirim.')
elif idade <= 14:
    print('Com essa idade, o atleta se enquadra na categoria Infantil.')
elif idade <= 19:
    print('Com essa idade, o atleta se enquadra na categoria Junior.')
elif idade <= 25:
    print('Com essa idade, o atleta se enquadra na categoria Sênior.')
else:
    print('Com essa idade, o atletla se enquadra na categoria Master.')

'''elif idade > 9 and idade <= 14:
    print('Com essa idade, o atleta se enquadra na categoria Infantil.')
elif idade > 14 and idade <= 19:
    print('Com essa idade, o atleta se enquadra na categoria Junior.')
elif idade > 19 and idade <= 25:
    print('Com essa idade, o atleta se enquadra na categoria Sênior.')
else:
    print('Com essa idade, o atletla se enquadra na categoria Master.')'''
