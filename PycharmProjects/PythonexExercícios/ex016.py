import math
n = float(input('Digite um numero com 3 casas decimais: '))
print('\033[34m')
print('O numero inteiro é {}.'.format(math.trunc(n)))
print('\033[m')