import random
#cores
cores = {'limpa': '\033[m',
         'amarelo': '\033[33m',
         'verde': '\033[32m'}
print(cores['amarelo'])
a1 = input('Digite o primeiro aluno: ')
a2 = input('Digite o segundo aluno: ')
a3 = input('Digite o terceiro aluno: ')
a4 = input('Digite o quarto aluno: ')
print(cores['limpa'])
lista = [a1, a2, a3, a4]
random.shuffle(lista) #comando para deixar uma lista em uma sequência aleatoria
print('A ordem é: {}{}{}'.format(cores['verde'] ,lista, cores['limpa']))




