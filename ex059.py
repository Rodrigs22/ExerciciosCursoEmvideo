#Biblioteca

import math
from time import sleep

#Meu codigo

#visual

print("**" * 30)
print("  INSIRA 2 NUMERO E DEPOIS DECIDA O QUE FAZER COM ELES")
print("**" * 30)
print("carregando...")
sleep(1)

#Variaveis

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print("carregando...")
sleep(1)

#algoritimo

print("Escolha o que deseja fazer com esses números\n"
          "[1] somar\n"
          "[2] multiplicar\n"
          "[3] maior\n"
          "[4] novos números\n"
          "[5] sair do programa")
opcao = int(input("Escolha:"))

while opcao != 5:

    if opcao == 1:
        resultado = numero1 + numero2
        print("O resultado é {}".format(resultado))

    elif opcao == 2:
        resultado = numero1 * numero2
        print("O resultado é {}".format(resultado))

    elif opcao == 3:
        resultado = max(numero1, numero2)
        print("O maior número é {}".format(resultado))

    elif opcao == 4:
        print("Digite novos números")
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))

    print("Escolha o que deseja fazer com esses números\n"
          "[1] somar\n"
          "[2] multiplicar\n"
          "[3] maior\n"
          "[4] novos números\n"
          "[5] sair do programa")
    opcao = int(input("Escolha:"))

    print("Carregando...")
    sleep(2)

print("Saindo...")
sleep(1)
print("Programa encerrado !")

