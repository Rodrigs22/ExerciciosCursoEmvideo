cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'verde': '\033[32m',}
nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A média do aluno {}{}{} é {}{}{}.'.format(cores['azul'], nome, cores['limpa'], cores['verde'], media, cores['limpa']))

