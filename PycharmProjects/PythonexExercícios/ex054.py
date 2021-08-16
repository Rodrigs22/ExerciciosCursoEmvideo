#Meu algoritimo
'''
cont = 0
cont2 = 0
for c in range(1, 8):
    idade = int(input('Digite a {} idade: '.format(c)))
    if idade >= 18:
        cont += 1
    else:
        cont2 += 1
print('{} pessoas ainda são menor de idade, e {} já são de maior.'.format(cont2, cont))
'''
#algoritimo do guanabara
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input('Digite a data de nascimento da {}° pessoas: '.format(pess)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
