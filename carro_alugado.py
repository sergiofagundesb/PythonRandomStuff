dias=int(input('Quantos dias o carro foi alugado?'))
km=float(input('Quantos km foram rodados?'))
preco=dias*60+0.15*km
print('O valor do aluguel ficou em R${:.2f}'.format(preco), end='\nPaga logo essa porra fdp')