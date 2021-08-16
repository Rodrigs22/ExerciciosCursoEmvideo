#meu algoritimo antigo
'''
peso1 = int(input('Digite seu peso: '))
peso2 = int(input('Digite seu peso: '))
peso3 = int(input('Digite seu peso: '))
peso4 = int(input('Digite seu peso: '))
peso5 = int(input('Digite seu peso: '))
lista = [peso1, peso2, peso3, peso4, peso5]
maior = max(lista)
menor = min(lista)
print('O menor peso apresentado foi {}'. format(menor))
print('O maior peso apresenrado foi {}'.format(maior))
'''
#algoritimo do guanabara
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Peso da {}° pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso apresentado foi, {}.'.format(maior))
print('O menor peso apresentado foi, {}.'.format(menor))
