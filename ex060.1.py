#algoritimo usando a biblioteca math

#bibliotecas
from math import factorial
from time import sleep

#visual

print("**" * 30)
print("   Descubra o fatorial de qualquer numero")
print("**" * 30)

print("Carregando...")
sleep(1)

numero = int(input("Digite o número que deseja ver o Fatorial: "))

print("Carregando...")
sleep(1)

fatorial = factorial(numero)

print("O fatorial do número {} é {}".format(numero, fatorial))

print("Encerrando o programa...")
sleep(1)
print("Programa encerrado! ")