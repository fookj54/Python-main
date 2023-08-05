real = float(input('Digite quanto você tem de R$: '))
dolar = real / 5.06
euro = real / 5.50
print('Seu dinheiro atual é: R$ {:.2f} \nVocê pode comprar até: US$ {:.2f} \nVocê pode comprar até: EUR$ {:.2f}'.format(real, dolar, euro))
