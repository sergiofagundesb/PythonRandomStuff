import random
n1 = input('Digite o nome do aluno número 1 ')
n2 = input('Digite o nome do aluno número 2 ')
n3 = input('Digite o nome do aluno número 3 ')
n4 = input('Digite o nome do aluno número 4 ')

lista = [n1,n2,n3,n4]

sorteio = random.choice(lista)
print('O aluno sorteado foi {}'.format(sorteio))

"""sorteado = int(random.randrange(1,4))
if sorteado == 1:
    print('O aluno {} foi sorteado'.format(n1))
elif sorteado == 2:
    print('O aluno {} foi sorteado'.format(n2))
elif sorteado == 3:
    print('O aluno {} foi sorteado'.format(n3))
elif sorteado == 4:
    print('O aluno {} foi sorteado'.format(n4))
=====[Isso foi feito da maneira mais burra possível]======="""