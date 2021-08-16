#cores
cores = {'limpa': '\033[m',
         'ciano': '\033[36m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}
#programa para descobrir se o número pe par ou impar
print(cores['ciano'])
num = int(input('Digite um numero para descobrir se ele é par ou impar: '))
print(cores['limpa'])
res = num % 2
if res == 0:
    print(cores['verde'], 'o Número é par !', cores['limpa'])
else:
    print(cores['vermelho'], 'O número é impar!', cores['limpa'])
print('--FIM--')
