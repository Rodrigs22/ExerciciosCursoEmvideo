#cores
cores = {'limpa': '\033[m',
         'amarelo': '\033[33m',
         'verde': '\033[32m'}
#equação
s = float(input('Qual o salario atual ? '))
d = float(input('Qual o aumento em porcentagem ? '))
eq = d * 0.01
va = eq * s
s = va + s
print('O salario com o aumento de {}{}{}% é R${}{}{} !'.format(cores['amarelo'], d, cores['limpa'], cores['verde'], s, cores['limpa']))
