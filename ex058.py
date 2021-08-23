#bibliotecas

from random import randrange
from time import sleep

# Parte visual de cima

print("--" * 20)
print("     JOGO DE ADIVINHAÇÃO")
print("--" * 20)

print("Carregando...")
sleep(1)

print("--" * 20)
print("   EU PENSEI EM ALGUM NUMERO ENTRE 1 E 10, TENTE ADIVINHAR")
print("--" * 20)

jogador = int(input("Faça sua escolha:"))   #input para armazenar a resposta do jogador
pc = randrange(1, 11)                #faz com que o pc escolha um numero importando randrange da bibliotéca random

#sistema de repetição até que o jogador acerte

cont = 1
while jogador != pc:                                #estrutura de repetição até o jogador acertar o nome
    print("Infelizmente você errou !")
    jogador = int(input("Tente novamente:"))
    cont += 1                                       #contador

sleep(1)

#quando o jogador acertar

print("Parabens, voce acertou após {} tentativas".format(cont))    #quando o jogador acerta