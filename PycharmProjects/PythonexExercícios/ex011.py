#cores
cores = {'limpa': '\033[m',
         'verde': '\033[32m',
         'vermelho': '\033[31m'}
#medir a área
a = float(input('Qual a altura ? '))
l = float(input('Qual a largura ? '))
area = a * l
s = area / 2
print('Sua parede tem a dimenssão de {}{}x{}{}, sua área é de {}{:.2f}m²{}'.format(cores['verde'], a, l, cores['limpa'], cores['verde'], area, cores['limpa']))
print('Para pintar será necessário {}{:.2f}{} litros de tinta !'.format(cores['vermelho'], s, cores['limpa']))


