#cores
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}
#transformar C° em F°
print(cores['verde'])
g = float(input('Digite a temperatura em Cº: '))
print(cores['limpa'])
eq = g * 1.8 + 32
print('{}{:.1f}{} em celsius, são {}{:.1f}{} em fahrenheit !'.format(cores['verde'], g, cores['limpa'], cores['vermelho'], eq, cores['limpa']))


