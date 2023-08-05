salario = float(input('Digite o seu salário: R$ '))

aumento = salario + (salario * 15/100)

print('Seu salário é: R$ {:.2f} \nSeu salário com aumento de 15% ficou: R$ {:.2f}'.format(salario, aumento))