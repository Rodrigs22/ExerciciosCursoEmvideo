cores = {'limpa': '\033[m',
         'ciano': '\033[36m',
         'roxo': '\033[35m',
         'amarelo': '\033[33m',
         'verde': '\033[32m'}
n = int(input('Escolha um numero: '))
print('O numero escolhido é {}{}{}, o dobro é {}{}{}, seu triplo é {}{}{} e sua raiz quadrada é {}{:.2f}{}'.format(cores['verde'], n, cores['limpa'], cores['ciano'], n*2, cores['limpa'], cores['roxo'], n*3, cores['limpa'], cores['amarelo'], n**(1/2), cores['limpa']))
