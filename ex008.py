m = float(input('Digite um valor em metros: '))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print('Sua metragem é : {:.1f} \nO valor em Quilômetro é: {} \nO valor em Hectômetro é: {} \nO valor de decâmetro é: {} \nO valor em decimetros é: {:.0f} \nO valor em centimetros é: {:.0f} \nO valor em milimetros é: {:.0f}'.format(m, km, hm, dam, dm, cm, mm))