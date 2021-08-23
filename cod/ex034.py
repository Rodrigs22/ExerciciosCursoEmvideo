#cores
cores = {'limpa': '\033[m',
         'ciano': '\033[36m',
         'azul': '\033[34m'}
#programa para calcular o aumento no salario
salario = float(input('Digite seu salario, R$: ')) #informando o valor recebido
if salario <= 1250:
    cal = (salario / 100) * 15 + salario
    print('{}Seu novo salario é dê R${:.2f}.{}'.format(cores['ciano'], cal, cores['limpa']))
else:
    cal = (salario / 100) * 10 + salario
    print('{}Seu novo salario é dê R${:.2f}.{}'.format(cores['azul'], cal, cores['limpa']))
print('--EXIT--')
