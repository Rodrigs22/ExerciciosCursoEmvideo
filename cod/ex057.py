#meu algoritimo
sexo = input('Digite seu sexo [M/F]: ').lower()
while sexo != 'm' and sexo != 'f':#usar o "and" em vez do "OR" para verificar se o valor digitado bate com algum dos dois
    sexo = input('valor invalido, digite novamente: ').lower()
print('obrigado pela informação')
