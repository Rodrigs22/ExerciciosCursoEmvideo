# cores
cores = {'limpa': '\033[m',
         'ciano': '\033[36m',
         'amarelo': '\033[33m',
         'verde': '\033[32m'}
# estética
print(cores['ciano'])
print('==' * 22)
print(cores['limpa'])
print(cores['amarelo'], 'Descubra se você pode financiar o imóvel', cores['limpa'])
print(cores['ciano'])
print('==' * 22)
print(cores['limpa'])
# programa para aprovar imprestimos
casa = float(input('Qual o valor da casa ? R$: '))
salario = float(input('Quanto você recebe mensalmente ? R$: '))
tempo = int(input('Em quantos meses você pretende pagar a casa ? '))
mensalidade = casa / tempo
sal = salario * 30 / 100
if sal >= mensalidade:
    print('Você pode financiar essa casa !')
else:
    print('Você não pode financiar essa casa !')
print('-exit-')