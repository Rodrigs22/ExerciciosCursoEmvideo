import math
#cores
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}
#calculando hipotenusa
print(cores['vermelho'])
ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('digite o valor do cateto oposto: '))
print(cores['limpa'])
h = math.hypot(ca, co)
print('A hipotenusa de CA {}{}{} e CO {}{}{}, é igual a {}{:.2f}{}.'.format(cores['vermelho'], ca, cores['limpa'], cores['vermelho'], co, cores['limpa'], cores['verde'], h, cores['limpa']))

