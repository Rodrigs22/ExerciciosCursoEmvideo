from time import sleep
from datetime import date
# cores
cores = {'limpa': '\033[m',
         'ciano': '\033[36m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}
# estética
print(cores['ciano'])
print('-=' * 22)
print(cores['limpa'])
print(cores['amarelo'])
print('DESCUBRA SE VOCÊ DEVE OU NÃO SE ALISTAR !')
print(cores['limpa'])
print(cores['ciano'])
print('-=' * 22)
print(cores['limpa'])
print('carregando...')
sleep(1)
# verificar se o individuo deve ou não se alistar
nome = str(input('Digite seu nome: ')).strip()
genero = str(input('Digite seu sexo (Masculino ou Feminino): ')).lower()
idade = int(input('informe seu ano de nascimento: '))
print('carregando...')
sleep(1)
atual = date.today().year
anos = atual - idade
difmais = anos - 18
difmenos = 18 - anos
if genero == 'feminino':
    print('Voce não precisa se alistar por ser mulher !')
elif genero == 'masculino' and anos > 18:
    print('Você esta {} ano(s) {}ATRASADO{} para se alistar !'.format(difmais, cores['vermelho'], cores['limpa']))
    print('Você devia ter se alistado em {}'.format(atual - difmais))
elif genero == 'masculino' and anos < 18:
    print('Ainda falta {}{} ano(s){} para você se alistar !'.format(cores['verde'], difmenos, cores['limpa']))
    print('O ano que você deve se alistar é {}.'.format(difmenos + atual))
elif genero == 'masculino' and anos == 18:
    print('Está na hora de voce se alistar, vá até um posto oficial para isso !')
print('-fim-')
