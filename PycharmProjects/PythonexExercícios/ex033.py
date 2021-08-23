import math
from time import sleep
#cores
cores = {'limpa': '\033[m',
         'ciano': '\033[36',
         'roxo': '\033[35m',
         'amarelo': '\033[33m'}
#programa para deobrir o menor e o maior numero
print(cores['ciano'])
num = float(input('Digite o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
num3 = float(input('Digite o terceiro numero: '))
print(cores['limpa'])
print('carregando...')
sleep(1)
m1 = max(num, num2, num3)
print(cores['amarelo'])
if num == m1:
    print('O número {} é o maior !'.format(num))
if num2 == m1:
    print('O numero {} é o maior !'.format(num2))
if num3 == m1:
    print('o número {} é o maior !'.format(num3))
print(cores['limpa'])
mini = min(num, num2, num3)
print(cores['roxo'])
if num == mini:
    print('O menor número é: {}'.format(num))
if num2 == mini:
    print('O menor numero é: {}'.format(num2))
if num3 == mini:
    print('O menor numero é: {}'.format(num3))
print(cores['limpa'])
print('--EXIT--')
