#meu algoritimo
'''
frase = str(input('Digite aqui a frase para saber se é um polindromo: ')).strip().lower().replace(' ', '')
invertida = frase[::-1]
if frase == invertida:
    print('Sim, essa frase é um polindromo !')
else:
    print('Não, essa frase não é um polindromo !')
'''
#algoritimo do guanabara
frase = str(input('Digite a frase para saber se ela é um polindromo: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso da frase {} é {}'.format(junto, inverso))
if junto == inverso:
    print('Essa frase é um polindromo.')
else:
    print('Essa frase não é um polindromo.')
