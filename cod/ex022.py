#cores
cores = {'limpa': '\033[m',
         'verde': '\033[32m',
         'ciano': '\033[36m'}
print(cores['verde'])
nome = (input('Digite seu nome: '))
print(cores['limpa'])
print(cores['ciano'])
print(nome.upper())
print(nome.lower())
var2 = nome.split()
var3 = ''.join(var2)
print(len(var3))
print(len(var2[0]))
print(cores['limpa'])

