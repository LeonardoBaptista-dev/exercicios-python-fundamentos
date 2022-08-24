medida = float(input(' Uma distância em metros: '))
cm = medida * 100
mm = medida * 1000
dm = medida * 10
m = medida * 1
dam = medida / 10
hm = medida / 100
km = medida / 1000
print('A medida de {}m corresponde a {:.0f}cm, {:.0f}mm, {:.0f}dm, {:.0f}dam, {:.0f}hm e {}km .'.format(medida, cm, mm, dm, dam, hm ,km))