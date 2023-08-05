dias = int(input('Quantos dias você alugou o carro? '))
km = float(input('Quantos Km você percorreu com o carro? '))
valor = (dias * 60) + (km * 0.15)
print('Valor a pagar pelo aluguel do carro é: R${:.2f}'.format(valor))
