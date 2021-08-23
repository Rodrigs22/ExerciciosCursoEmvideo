from time import sleep
#cores
cores = {'limpa': '\033[m',
         'ciano': '\033[36m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}
#estética
print(cores['ciano'], '--' * 15, cores['limpa'])
print(cores['vermelho'], 'taboada até o 10', cores['limpa'])
print(cores['ciano'], '--' * 15, cores['limpa'])
print('loading...')
sleep(1)
#taboada
n = int(input('Digite o numero que você quer ver a tabuada: '))
print('calculando...')
sleep(1)
print(cores['verde'])
print(n, 'x 1 =', n*1)
print(n, 'x 2 =', n*2)
print(n, 'x 3 =', n*3)
print(n, 'x 4 =', n*4)
print(n, 'x 5 =', n*5)
print(n, 'x 6 =', n*6)
print(n, 'x 7 =', n*7)
print(n, 'x 8 =', n*8)
print(n, 'x 9 =', n*9)
print(n, 'x 10 =', n*10, cores['limpa'])
