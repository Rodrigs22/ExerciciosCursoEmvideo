numero = int(input('digite um numero inteiro para transformar: '))
c1 = int(input('''[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
Escolha: '''))
if c1 == 1:
    print('O numero {} convertido em binário é, {}.'.format(numero, bin(numero)[2:]))
elif c1 == 2:
    print('o Numero {} convertido em octal é, {}.'.format(numero, oct(numero)[2:]))
elif c1 == 3:
    print('O numero {} convertido em Hexadecimal é, {}.'.format(numero, hex(numero)[2:]))
else:
    print('opção invalida, tente novamente!')