#Programa para calcular se a pessoa precisa ou não se alistar
from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano do seu nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))
if idade == 18:
    print('Você precisa se alistar imediatamente!')
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Como passou {} anos da sua data de tempo de alistamento, você deve procurar a junta militar o quanto antes.'.format(saldo))
    print('Seu alistamento foi no ano de {}.'.format(ano))
elif idade < 18:
    saldo = 18 - idade
    ano = atual + saldo
    print('Faltam {} anos para você completar a idade para alistamento Militar.'.format(saldo))
    print('Seu alistamento será no ano de {}.'.format(ano))
