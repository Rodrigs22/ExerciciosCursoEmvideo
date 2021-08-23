#cores
cores = {'limpa': '\033[m',
         'ciano': '\033[36m',
         'verde': '\033[32m'}
#calculo do alugel
d = float(input('por quantos dias o carro esteve alugado: '))
km = float(input('Quando KM o carro rodou: '))
eqd = d * 60
eqk = km * 0.15
vf = eqd + eqk
print('O carro foi alugado por {}{}{} dias e rodou por {}{}{} Km, nesse caso o aluguel foi dê {}R${:.2f}{}.'.format(cores['ciano'], d, cores['limpa'], cores['ciano'], km, cores['limpa'], cores['verde'], vf, cores['limpa']))
