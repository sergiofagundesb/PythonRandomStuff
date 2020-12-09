from math import sqrt,sin,cos,asin,acos,degrees,hypot
a = float(input('Digite o cateto oposto'))
b = float(input('Digite o cateto adjacente'))
#c = sqrt((a**2) + (b**2))
c = hypot(a,b)
print('A hipotenusa desse triângulo é {:.2f}'.format(c))
print('O seno é, portanto {}'.format(sin(b/c)))
print('São portanto {} graus'.format(degrees(asin(b/c))))