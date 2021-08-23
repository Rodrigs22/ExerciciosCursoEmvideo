#meu jeito
'''
from time import sleep
v = str(input('Seleciona a opção desejavel. #eu tirei as 3 aspas para deixa o programa como comentario!!!!!
[ x ] inicia
[ z ] desliga
: ')).strip().lower()
if v == 'x':
    s = 0
    for c in range(3, 501, 6):
        s += c
    print('a soma total é: {}'.format(s))
    print('carregando...')
    sleep(2)
    print('
    [ x ] ver os numeros
    [ z ] desligar')
    z = str(input('escolha a opção desejada: ')).strip().lower()
    if v == 'x':
        for c in range(3, 501, 6):
            print(c)
        sleep(1)
        print('desligando...')
        sleep(1)
        print('desligado')
    else:
        print('desligando...')
        sleep(1)
        print('desligado')
else:
    print('desligando...')
    sleep(1)
    print('desligado')
'''

#jeito do guanabara

cont = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma dos {} apresentados é {}.'.format(cont, soma))
