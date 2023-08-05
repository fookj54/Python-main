from math import sqrt
cat_Oposto = float(input('Qual o cateto oposto: '))
cat_Adjacente = float(input('Qual o cateto adjacente: '))
hipotenusa = sqrt(cat_Oposto **2 + cat_Adjacente ** 2)

print('A hipotenusa dos cateto Oposto {} e cateto Adjacente {} é: \n{:.2f}'.format(cat_Oposto, cat_Adjacente, hipotenusa))
