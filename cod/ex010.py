cores = {'limpa': '\033[m',
         'verde': '\033[32m'}
d = float(input('Quantos reais você deseja gastar com Dolar ?'))
m = d / 3.27
print('Com {}{:.2f}{} reais, você consegue comprar {}{:.2f}{} dolares!'.format(cores['verde'], d, cores['limpa'], cores['verde'], m, cores['limpa']))
