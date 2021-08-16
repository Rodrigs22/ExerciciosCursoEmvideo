#meu algoritimo
from random import randrange
pc = randrange(0, 10)
jogador = int(input('Pense em um numero de 0 á 10: '))
tentativas = 1
while jogador != pc:
    if jogador > 10 or jogador < 0:
        jogador = int(input('Opção invalida, só vale entre 0 e 10, digite novamente: '))
        tentativas += 1
    elif jogador != pc:
        jogador = int(input('Voce errou, tente novamente: '))
        tentativas += 1
print('Você acertou após {} tentativas !'.format(tentativas))
