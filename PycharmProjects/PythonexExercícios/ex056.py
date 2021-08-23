#meu algoritimo (incompleto, não consegui terminar
'''
soma = 0
cont = 0
maior = 0
for p in range(1, 5):
    nome = input('Digite o nome da {}° pessoa: '.format(p))
    idade = int(input('Digite a idade da {}° pessoa: '.format(p)))
    sexo = input('Digite o sexo da {}°, (masculino ou feminino) pessoa: '.format(p)).strip().lower()
    soma = (soma + idade) / 2
    if sexo == 'masculino':
        maior = idade
    if idade > maior:
            print(nome)
print('A média de idade do grupo é {:.0f} anos.'.format(soma))
'''
#algoritimo do guanabara
soma = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for p in range(1, 5):
    print('-----{}° pessoa------'.format(p))
    nome = input('Digite o nome da {}° pessoa: '.format(p))
    idade = int(input('Digite a idade da {}° pessoa: '.format(p)))
    sexo = input('Selecione o sexo [F/M]: ').strip().lower()
    soma += idade
    if p == 1 and sexo == 'm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'f' and idade < 20:
        totmulher20 += 1
mediaidade = soma / 4
print('A média da idade do grupo é {:.1f} anos.'.format(mediaidade))
print('O Homem mais velho tem a idade de {} e se chama {}.'.format(maioridadehomem, nomevelho))
print('Tem {} mulher(es) com menos de 20 anos.'.format(totmulher20))
