n=float(input('Digite um número'))
print('O número {} tem seu dobro {}, triplo {}, e raiz quadrada {}'.format(n,(2*n),(3*n),(n**(1/2))))
print('='*20)
n1=float(input('Digite o primeiro número'))
n2=float(input('Digite o segundo número'))
media=(n1+n2)/2
if media >= 5:
    print('Aprovado')
if media < 5:
    print('Reprovadíssimo')
print('A média aritimética entre {:.1f} e {:.1f} é {:.1f}'.format(n1,n2,media))

