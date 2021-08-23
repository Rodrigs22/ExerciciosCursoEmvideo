#Meu algoritimo
'''
termo = int(input('Digite o prmeiro termo da PA: '))
razao = int(input('Digite a razao da PA: '))
quantidade = int(input('Digite quantos termos quer ver: '))
ultimo = termo + (quantidade-1)*razao
ultimo = ultimo + 1
for c in range(termo, ultimo, +razao):
    print(c)
print('Fim')
'''
#Algoritimo do guanabara
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
ultimo = primeiro + (10 - 1) * razao
for c in range(primeiro, ultimo + razao, razao):
    print('{} '.format(c), end='-> ')
print('acabou')