from random import choice
from time import sleep
# cores
cores = {'limpa': '\033[m',
         'ciano': '\033[36m',
         'verde': '\033[32m'}
# estética
print(cores['ciano'])
print('-=' * 22)
print(cores['limpa'])
print(cores['verde'])
print(' VAMOS JOGAR JOKENPO')
print('PROMETO NÃO TRAPACEAR!')
print(cores['limpa'])
print(cores['ciano'])
print('-=' * 22)
print(cores['limpa'])
print('carregando o jogo...')
sleep(1)
# programa que joga jokenpo com você
lista = ['pedra', 'papel', 'tesoura']
escolha = choice(lista)
print('''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Escolha: '))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ !!!')
if jogador == 0 and escolha == 'tesoura':
    print('você escolheu: {}'.format('PEDRA'))
    print('eu escolhi {}'.format(escolha))
    print('Droga ! dessa vez você ganhou !')
elif jogador == 2 and escolha == 'papel':
    print('você escolheu: {}'.format('TESOURA'))
    print('eu escolhi {}'.format(escolha))
    print('Droga ! dessa vez você ganhou !')
elif jogador == 1 and escolha == 'pedra':
    print('você escolheu: {}'.format('PAPEL'))
    print('eu escolhi {}'.format(escolha))
    print('Droga ! dessa vez você ganhou !')
elif escolha == 'pedra' and jogador == 2:
    print('você escolheu: {}'.format('TESOURA'))
    print('eu escolhi {}'.format(escolha))
    print('HAHA, eu GANHEI !')
elif escolha == 'tesoura' and jogador == 1:
    print('você escolheu: {}'.format('PAPEL'))
    print('eu escolhi {}'.format(escolha))
    print('HAHA, eu GANHEI !')
elif escolha == 'papel' and jogador == 0:
    print('você escolheu: {}'.format('PEDRA'))
    print('eu escolhi {}'.format(escolha))
    print('HAHA, eu GANHEI !')
else:
    print('eu também escolhi {}'.format(escolha))
    print('Empatamos ! vamos tentar denovo ?')
