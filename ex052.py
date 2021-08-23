#meu algoritimo
'''
n = int(input('Digite um numero para saber se ele primo: '))
if n == 2 or n == 3 or n == 5 or n == 7 or n == 11 or n == 13 or n == 17 or n == 19 or n == 23: #usando alguns primos declarados
    print('primo')
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 11 == 0 or n % 13 == 0 or n % 17 == 0 or n % 19 == 0 or n % 23 == 0: # passando um pente fino
    print('Não é primo')
else:
    print('é primo !')
'''
#algoritimo do guanabara
num = int(input('Digite um número para saber se ele é primo: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(num, tot))
if tot == 2:
    print('esse numero é primo !')
else:
    print('Esse numero não é primo !')
