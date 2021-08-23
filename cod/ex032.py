from datetime import date# biblioteca para informar o dia atual para a maquina
#cores
cores = {'limpa': '\033[m',
         'ciano': '\033[36m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}
#programa para decobrir se o ano é bissexto
print(cores['ciano'])
ano = int(input('Digite o ano para saber se ele é bissexto, digite 0 para selecionar o ano atual !: '))
print(cores['limpa'])
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:#equação para descobrir
    print(cores['verde'], 'esse ano é bissexto !', cores['limpa'])
else:
    print(cores['vermelho'], 'esse ano não é bissexto !', cores['limpa'])
print('--FIM--')
