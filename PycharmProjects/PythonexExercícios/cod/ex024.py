#cores
cores = {'limpa': '\033[m',
         'ciano': '\033[36m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}
#descobrir se a sua cidade começa ou não com >>SANTO<<
'''print(cores['ciano'])
cidade = input('Digite o nome da sua cidade: ')
print(cores['limpa'])
teste = cidade.lower()
teste2 = teste.strip()
var = teste2.split()
print(cores['vermelho'])
print('santo' in var[0])
print(cores['limpa'])'''

print(cores['ciano'])
cidade  = input('Digite o nome da sua cidade: ')
print(cores['limpa'])
teste = cidade.lower()
teste2 = teste.strip()
teste3 = teste2.split()
if 'santo' in teste3[0]:
    print(cores['verde'] ,'Sim, sua cidade começa com SANTO', cores['limpa'])
else:
    print(cores['vermelho'] ,'não, sua cidade não começa com SANTO', cores['limpa'])