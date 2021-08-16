#cores
cores = {'limpa': '\033[m',
         'roxo': '\033[35m'}
p = float(input('Qual o preço sem desconto ? '))
d = float(input('Qual o desconto em porcentagem ? '))
eq = d * 0.01
vd = eq * p
s = p - vd
print('{}O preço do produto depois do dessconto é {} !{}'.format(cores['roxo'], s, cores['limpa']))

