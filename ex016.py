#Usando método de importação de módulo 
from math import trunc
valor = float(input('Digite um valor: '))
print('O valor digitado foi: {} e a sua porção inteira é {}'.format(valor, trunc(valor)))

#Outra forma de resolver
print('O valor digitado foi: {} e a sua porção inteira é {}'.format(valor, int(valor)))
