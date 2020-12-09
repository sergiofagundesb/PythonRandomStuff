import math
ang = float(input('Digite o ângulo em graus'))
print('O seno é {:.2f}, o cosseno é {:.2f}, a tangente é {:.2f} e o ângulo é {:.2f}'.
format(math.sin(math.radians(ang)),
math.cos(math.radians(ang)),math.tan(math.radians(ang)),ang))
