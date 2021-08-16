#meu jeito de fazer
'''
soma = 0 #forma de somar um laço
for c in range(0, 6):
    n = int(input('Digite o valor'))
    if n % 2 == 0: #equação para saber se é par
        soma = soma + n #forma de somar um laço
print(soma)
'''
#algoritomo do guanabara
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {} numero: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('me foi apresentado {} numero(s) par(es), e a soma deles é {}.'.format(cont, soma))