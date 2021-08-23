pritermo = int(input('digite o primeiro termo: '))
razao = int(input('Digite o segundo termo: '))
quanttermos = int(input('Digite quantos termos deseja ver: '))
cont = 1
while cont <= quanttermos:
    print('{} --> '.format(pritermo), end='')
    pritermo += razao
    cont += 1
print('fim')
