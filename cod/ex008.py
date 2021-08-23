m = int(input('Digite a medida em metros: '))
print('\033[36;41m', 'O valor escolhido em metro é {}, \nem CM é igual a {} \ne em Milimetros é igual a {}', '\033[m'.format(m, m*100, m*1000))

