#cores
cores = {'limpa': '\033[m',
         'branco': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m'}
#programa que calcula quanto vai custar a viagem, baseado no Kilimetro
dis = float(input('Quantos Km tem sua viagem ?: '))
if dis <= 200:
    cal = dis * 0.5
    print('{}Sua viagem vai custar R${:.2f}{}'.format(cores['verde'], cal, cores['limpa']))
else:
    cal = dis * 0.45
    print('{}Sua viagem vai custar R${:.2f}{}'.format(cores['vermelho'], cal, cores['limpa']))
print('--FIM--')
