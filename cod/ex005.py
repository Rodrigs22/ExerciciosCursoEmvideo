n = int(input('Digite um valor: '))
print('O número escolhido é {}{}{}, seu antecessor é {}{}{} e seu sucessor é {}{}{}.'.format('\033[32m', n, '\033[m', '\033[36m',  n-1, '\033[m', '\033[35m', n+1, '\033[m'))
