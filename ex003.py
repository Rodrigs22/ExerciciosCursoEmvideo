cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
s = n1 + n2
print('A soma entre {}{}{} e {}{}{} é igual a {}{}{}.'.format(cores['vermelho'], n1, cores['limpa'], cores['vermelho'], n2, cores['limpa'], cores['verde'], s, cores['limpa']))
