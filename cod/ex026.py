from time import sleep
#cores
cores = {'limpa': '\033[m',
         'roxo': '\033[35m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'azul': '\033[34m'}
print(cores['amarelo'])
print('<>' * 22)
print(cores['limpa'])
print(cores['vermelho'])
print('Verifique quantas letras "A" tem no texto')
print(cores['limpa'])
print(cores['amarelo'])
print('<>' * 22)
print(cores['limpa'])
print('carregando...')
sleep(2)
#contando letras A
print(cores['azul'])
texto = input('Digite seu texto: ').strip()
print('carregando...')
sleep(2)
print(cores['limpa'])
form = texto.lower()
vezes = form.count('a')
print(cores['roxo'])
print('a letra A aparece {} vez(es).'.format(vezes))
print(cores['limpa'])
print(cores['azul'])
print('A letra A aparece a primeira vez na posição {}.'.format(form.find('a')+1))
print(cores['limpa'])
print(cores['vermelho'])
print('A letra A aparece pela ultima vez na posição {}. '.format(form.rfind('a')-1))
print(cores['limpa'])



