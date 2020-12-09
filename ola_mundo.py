valor= int(input('Digite a escala que deseja converter. 1 para Celsius e 2 para Fahreinheit'))
if valor < 2:

    temperatura = float(input('Digite a temperatura em ºC'))
    retorno = float((temperatura * 9 + 160)/ 5)
    print('{}ºC são {}ºF'.format(temperatura, retorno))
else:
    temperatura = float(input('Digite a temperatura em ºF'))
    retorno = float((temperatura * 5 - 160)/9)
    print('{}ºF são {}ºC'.format(temperatura, retorno))

