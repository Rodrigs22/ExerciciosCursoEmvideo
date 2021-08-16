'''
num = input('Digite um número de até 9999: ')
print('Unidade:{} '.format(num[3]))
print('Dezena:{} '.format(num[2]))
print('Centena:{} '.format(num[1]))
print('Milhar:{} '.format(num[0]))
'''
from time import sleep
#cores
cores = {'limpa': '\033[m',
         'ciano': '\033[36m',
         'amarelo': '\033[33m',
         'roxo': '\033[35m',
         'branco': '\033[30m'}
print(cores['ciano'])
print('@' * 22)
print(cores['limpa'])
print(cores['amarelo'])
print(' SEPARADOR DE VALORES')
print(cores['limpa'])
print(cores['ciano'])
print('@' * 22)
print(cores['limpa'])
print('Carregando...')
sleep(1)
#equação para calcular - UNIDADE - DECIMAL - CENTENA - MILHAR
num = int(input('Digite um numero: '))
print('carregando...')
sleep(1)
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(cores['ciano'])
print('Unidade: {}'.format(u))
print(cores['limpa'])
print(cores['amarelo'])
print('Dezena: {}'.format(d))
print(cores['limpa'])
print(cores['roxo'])
print('Centena: {}'.format(c))
print(cores['limpa'])
print(cores['branco'])
print('milhar: {}'.format(m))
print(cores['limpa'])