print('Calculadora de juros')
a = int(input('Digite 1 para juros compostos e 2 para juros simples'))
if a== 1:
    c = float(input('Digite o Capital Inicial '))
    t = float(input('Digite a taxa de juros em %' ))
    p = int(input('Digite p número de prestações/parcelas'))
    m = float(c*(1+t/100)**p)
    print('O valor final será de {}'.format(m))
if a == 2:
    print('2')

#192