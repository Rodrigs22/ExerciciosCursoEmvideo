from datetime import date
nome = str(input('Digite seu nome: ')).strip()
idade = int(input('Digite o ano em que você nasceu (4 digitos): '))
ano = date.today().year
# idp = idade do participante
idp = ano - idade
if idp <= 9:
    print('nome: {}'.format(nome))
    print('idade: {}'.format(idp))
    print('Classificação: MIRIM')
elif idp > 9 and idp <= 14:
    print('nome: {}'.format(nome))
    print('idade: {}'.format(idp))
    print('Classificação: INFANTIL')
elif idp > 14 and idp <= 19:
    print('nome: {}'.format(nome))
    print('idade: {}'.format(idp))
    print('Classificação: JUNIOR')
elif idp > 19 and idp <= 20:
    print('nome: {}'.format(nome))
    print('idade: {}'.format(idp))
    print('Classificação: SÊNIOR')
elif idp > 20:
    print('nome: {}'.format(nome))
    print('idade: {}'.format(idp))
    print('Classificação: MASTER')
