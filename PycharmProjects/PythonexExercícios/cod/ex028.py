import random
from time import sleep
'''
num = random.randrange(1, 5)
numero = int(input('Digite um numero ebtre 1 e 5: '))
if numero == num:
    print('Você acertou, PARABENS!!')
else:
    print('Que pena, você errou !')
print('--FIM--')
'''
#cores
cores = {'limpa': '\033[m',
         'ciano': '\033[36m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'verde': '\033[32m',
         'vermelho': '\033[31m'}
#jogo de advinhação
print(cores['ciano'])
print('-=-' * 20)
print(cores['limpa'])
print(cores['amarelo'])
print('Vou pensar em um número entre 0 e 5, tente adivinhar !')
print(cores['limpa'])
print(cores['ciano'])
print('-=-' * 20)
print(cores['limpa'])
print('carregando...')
sleep(1)
pc = random.randrange(0, 5)
jg = int(input('Escolha seu número entre 0 e 5: '))
print('ESCOLHENDO UM NUMERO...')
sleep(2)
if pc == jg:
    print(cores['verde'])
    print('Parabéns eu realmente pensei no numero {}'.format(pc))
    print(cores['limpa'])
else:
    print(cores['vermelho'])
    print('Que pena eu pensei no número {} e não no {}'.format(pc, jg))
    print(cores['limpa'])
print('--FIM--')
