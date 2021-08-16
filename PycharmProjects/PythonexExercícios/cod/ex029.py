from time import sleep
#cores
cores = {'limpa': '\033[m',
         'ciano': '\033[36m',
         'amarelo': '\033[33m',
         'roxo': '\033[35m',
         'verde': '\033[32m',
         'vermelho': '\033[31m'}
#estética
print(cores['ciano'])
print('**' * 22)
print(cores['limpa'])
print(cores['amarelo'], '   ROBÔ DE MULTA AUTOMATICO', cores['limpa'])
print(cores['ciano'])
print('**' * 22)
print(cores['limpa'])
print('carregando programa...')
sleep(1)
#calculadora de multa baseada na velocidade
print(cores['ciano'])
vel = int(input('Digite a velocidade do carro: '))
print(cores['limpa'])
if vel > 80:
    mul = (vel - 80) * 7
    print('Você foi multado no valor dê R${}{:.2f}{} devido o excesso de velocidade!'.format(cores['vermelho'], mul, cores['limpa']))
else:
    print(cores['verde'])
    print('Você está dirigindo com segurança ! parabens !')
    print(cores['limpa'])
print('-EXIT-')