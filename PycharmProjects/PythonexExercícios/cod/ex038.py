num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
if num1 > num2:
    print('O numero {} é o maior !'.format(num1))
    print('O numero {} é o menor !'.format(num2))
elif num2 > num1:
    print('O numero {} é o maior'.format(num2))
    print('O menor numero é o {}'.format(num1))
else:
    print('Os valores são iguais !')
