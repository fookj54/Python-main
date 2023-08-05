from math import sin, cos, tan, radians
angulo = float(input('Digite o ângulo que você deseja: '))
seno = sin (radians (angulo))
cosseno = cos (radians (angulo))
tangente = tan (radians (angulo))

print('O ângulo de {} tem: \nSeno de {:.2f} \nCosseno de {:.2f} \nTangente de {:.2f}'.format(angulo, seno, cosseno, tangente))
