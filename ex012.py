valor = float(input('Digite o valor do produto: R$ '))
desc_cinco = valor - (valor * 5/100)
print('Valor do produto: {:.2f} \nO valor com 5% de desconto é: {:.2f}'.format(valor, desc_cinco))