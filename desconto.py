preco=int(input('Digite o preço'))
desconto=float(input('Digite o desconto em %'))
print('O produto que antes custava R${}, agora com desconto de {}% custa R${}'.format(preco,desconto,(1-(desconto/100))*preco))
