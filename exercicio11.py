largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))
área = largura * altura
tinta = área / 2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².\nPara pintar sua parede, você precisará de {}l de tinta.'.format(largura, altura, área, tinta))