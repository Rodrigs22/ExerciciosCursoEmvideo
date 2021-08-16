from random import choice
#cores
cores = {'limpa': '\033[m',
         'amarelo': '\033[33m',
         'ciano': '\033[36m',
         'verde': '\033[32m'}
#programa de seleção
print(cores['amarelo'])
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
print(cores['limpa'])
lista = [a1, a2, a3, a4]
escolhido = choice(lista) #comando para selecionar 1 entre uma lista
print('O aluno escolhido é: {}{}{}'.format(cores['verde'] ,escolhido, cores['limpa']))

