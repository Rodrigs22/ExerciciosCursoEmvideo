#codigo sem usar a função factorial da biblioteca

#bibliotecas
from time import sleep

#visual

print("**" * 30)
print("   Descubra o fatorial de qualquer numero")
print("**" * 30)

print("Carregando...")
sleep(1)

numero = int(input("Digite o número que deseja ver o Fatorial: "))
cont2 = numero

print("Carregando...")
sleep(1)

cont = 1
while cont2 != cont:
    numero = numero * cont
    cont += 1

print("O fatorial de {} é {}.".format(cont2, numero))

print("Encerrando o programa...")
sleep(1)
print("Programa encerrado! ")