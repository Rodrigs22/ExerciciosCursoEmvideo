nome = input('Digite alguma coisa: ')
print('\033[33m', 'Classe: {}'.format(type(nome)))
print('É maiuscula? ', nome.isupper())
print('É minuscula?', nome.islower())
print('Tem espaço?', nome.isspace())
print('istitle?', nome.istitle())
print('isalpha?', nome.isalpha())
print('isprintable?', nome.isprintable())
print('isdecimal?', nome.isdecimal())
print('isdigit?', nome.isdigit())
print('isascii?', nome.isascii())
print('isidentifier?', nome.isidentifier())
print('isalnum? ', nome.isalnum())
print('isnumeric?', nome.isnumeric())
print('subclass', nome.__init_subclass__(), '\033[m')
