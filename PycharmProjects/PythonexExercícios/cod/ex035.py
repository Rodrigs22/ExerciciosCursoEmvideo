#cores
cores = {'limpa': '\033[m',
         'ciano': '\033[36m',
         'amarelo': '\033[33m',
         'verde': '\033[32m',
         'vermelho': '\033[31m',
         'roxo': '\033[35m'}
#estética
print(cores['verde'])
print('oo' * 22)
print(cores['limpa'])
print(cores['ciano'], 'Descubra se as retas formam um triangulo !', cores['limpa'])
print(cores['verde'])
print('oo' * 22)
print(cores['limpa'])
#programa para descobrir se as 3 retas informadas formam um triangulo
print(cores['ciano'])
r1 = float(input('Digite o valor da primeira reta: '))
print(cores['limpa'])
print(cores['amarelo'])
r2 = float(input('Digite o valor da segunda reta: '))
print(cores['limpa'])
print(cores['roxo'])
r3 = float(input('Digite o valor da terceira reta: '))
print(cores['limpa'])
if r1 - r2 < r3 < r1 + r2:
    print(cores['verde'], 'Essas medidas formam um triangulo !', cores['limpa'])
else:
    print(cores['vermelho'], 'Essas medidas não foramam um triangulo!', cores['limpa'])
print('--EXIT--')

