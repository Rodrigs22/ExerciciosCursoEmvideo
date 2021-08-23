import math
#cores
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'roxo': '\033[35m',
         'ciano': '\033[36m'}
#equação
an = float(input('digite o ângulo aqui: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tg = math.tan(math.radians(an))
print(cores['ciano'])
print('O angulo escolhido é {}, seu SENO é:{:.2f} '.format(an, seno))
print(cores['limpa'])
print(cores['roxo'])
print('O angulo escolhido é {}, seu COSSENO é:{:.2f} '.format(an, cosseno))
print(cores['limpa'])
print(cores['azul'])
print('O angulo escolhido é {}, sua TANGENTE é:{:.2f} '.format(an, tg))
print(cores['limpa'])