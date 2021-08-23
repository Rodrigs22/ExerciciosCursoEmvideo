'''
#meu algoritimo usando laço
numero = int(input('Digite o número que você quer saber o fatorial: '))
fat = 1
for f in range(1, numero+1):
    fat *= f
print(fat)
'''
#usando while
'''
num = int(input('Digite o numero que deseja saber o fatorial: '))
c = 1
fat = 1
while c <= num:
    fat *= c
    c += 1
print(fat)
'''
#usando biblioteca
from math import factorial
num = int(input('Digite um numero: '))
fac = factorial(num)
print(fac)