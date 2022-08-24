nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(nota1,nota2,media))
if media >= 7.0:
    print('Você está aprovado.')
elif media >= 5 and media < 7:
    print('Você está em recuperação.')
elif media < 5.0:
    print('Você foi reprovado. ')
