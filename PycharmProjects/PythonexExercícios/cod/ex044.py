valor = float(input('Digite o valor do produto: R$ '))
print('Escolha a forma de pagamento ')
pag = str(input('dinheiro ou cartão: ')).strip().lower()
if pag == 'dinheiro':
    des = (valor * 10) / 100
    desconto = valor - des
    print('O valor total é de R$ {}. Com 10% de desconto'.format(desconto))
elif pag == 'cartão' or pag == 'cartao':
    v = int(input('Digite em quantas parcelas deseja pagar: '))
    if v == 1:
        des = (valor * 5) / 100
        desconto = valor - des
        print('O valor total é dê R${}, com 5% de desconto.'.format(desconto))
    elif v == 2:
        parcela = valor / 2
        print('O valor total é dê R${}, sem nenhum desconto.'.format(valor))
        print('O valor de cada parcela é dê R${}.'.format(parcela))
    elif v > 2:
        au = (valor * 20) / 100
        aumento = valor + au
        parcela = aumento / v
        print('O valor total é dê R${}, com 20% de juros !.'.format(aumento))
        print('O valor de cada parcela é dê R${}'.format(parcela))
print('Obrigado por comprar conosco !')