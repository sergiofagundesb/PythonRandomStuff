import math
print('=========[Calculadora de equações de segundo grau')

a = float(input('Digite o coeficiente a '))
b = float(input('Digite o coeficiente b '))
c = float(input('Digite o coeficiente c '))
delta = pow(b,2)-4*a*c
#print('o valor de delta foi ',delta)

if delta < 0:
    print('Solução fora do conjunto dos números reais')
    delta = delta*-1
    delta_complexo = math.sqrt(delta)/2*a
    x1real = (-b/2*a)
    print('O valor de x1 é um complexo {} + {}i'.format(x1real,delta_complexo))
    print('O valor de x2 é um complexo {} - {}i '.format(x1real,delta_complexo))
else:
    x1_real = (-b+ math.sqrt(delta))/2*a
    x2_real = (-b- math.sqrt(delta))/2*a
    print('O valor de x1 é {} e de x2 é {}'.format(x1_real,x2_real))
