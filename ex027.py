#cores
cores = {'limpa': '\033[m',
         'amarelo': '\033[33m',
         'verde': '\033[32m',
         'ciano': '\033[36m'}
#separa seu primeiro nome do último
print(cores['ciano'])
nome = input('Digite seu nome: ')
print(cores['limpa'])
var = nome.strip()
var2 = var.split()
print(cores['verde'])
print('Primeiro nome: {}'.format(var2[0]))
print(cores['limpa'])
print(cores['amarelo'])
print('Ultimo nome: {}'.format(var2[-1]))
print(cores['limpa'])



