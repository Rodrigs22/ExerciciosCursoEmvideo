#MEU ALGORITIMO
from time import sleep
print('--' * 20)
print('          Digite 2 valores')
print('--' * 20)
num1 = float(input('Digite o 1° numero: '))
num2 = float(input('Digite o 2° numero: '))
escolha = ''
while escolha != 5:
    escolha = int(input('''
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] Maior valor
    [ 4 ] novos Numeros
    [ 5 ] sair
    : '''))
    if escolha == 4:
        num1 = float(input('Digite o 1° valor: '))
        num2 = float(input('Digite o 2° valor: '))
    if escolha == 1:
        soma = num1 + num2
        print('O resultado da soma é {}.'.format(soma))
    elif escolha == 2:
        mult = num1 * num2
        print('O resultado da multiplicação é {}.'.format(mult))
    elif escolha == 3:
        if num1 > num2:
            maior = num1
            print('O maior valor é o {}.'.format(maior))
        elif num2 > num1:
            maior = num2
            print('O maior valor é o {}.'.format(maior))
        else:
            print('Os valores são iguais !')
print('Encerrando o programa...')
sleep(1)
print('Encerrado !')
