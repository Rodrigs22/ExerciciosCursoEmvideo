#cores
cores = {'limpa': '\033[m',
         'amarelo': '\033[33m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'ciano': '\033[36m'}
#estética
print(cores['amarelo'])
print('-=' * 22)
print(cores['limpa'])
print(cores['ciano'])
print('CALCULE A MÉDIA DO SEU ALUNO !')
print(cores['limpa'])
print(cores['amarelo'])
print('-=' * 22)
print(cores['limpa'])
# programa para calcular a média do aluno
quantidade = int(input('digite quantas notas serão usadas para avaliar (MIN 2, MAX 4): '))
if quantidade == 2:
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    media = (n1 + n2) / 2
    if media >= 7:
        print('{}Sua nota foi dê {}, você foi APROVADO !{}'.format(cores['verde'], media, cores['limpa']))
    elif media >= 5 < 7:
        print('{}Sua nota foi dê {}, você esta de recuperação{}'.format(cores['amarelo'], media, cores['limpa']))
    else:
        print('{}Sua nota foi dê {}, você foi reprovado !{}'.format(cores['vermelho'], media, cores['limpa']))
    print('{}Desejamos um bom dia a todos !{}'.format(cores['ciano'], cores['limpa']))
elif quantidade == 3:
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))
    media = (n1 + n2 + n3) / 3
    if media >= 7:
        print('{}Sua nota foi dê {}, você foi APROVADO !{}'.format(cores['verde'], media, cores['limpa']))
    elif media >= 5 < 7:
        print('{}Sua nota foi dê {}, você esta de recuperação{}'.format(cores['amarelo'], media, cores['limpa']))
    else:
        print('{}Sua nota foi dê {}, você foi reprovado !{}'.format(cores['vermelho'], media, cores['limpa']))
    print('{}Desejamos um bom dia a todos !{}'.format(cores['ciano'], cores['limpa']))
elif quantidade == 4:
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))
    n4 = float(input('Digite a quarta nota: '))
    media = (n1 + n2 + n3 + n4) / 4
    if media >= 7:
        print('{}Sua nota foi dê {}, você foi APROVADO !{}'.format(cores['verde'], media, cores['limpa']))
    elif media >= 5 < 7:
        print('{}Sua nota foi dê {}, você esta de recuperação{}'.format(cores['amarelo'], media, cores['limpa']))
    else:
        print('{}Sua nota foi dê {}, você foi reprovado !{}'.format(cores['vermelho'], media, cores['limpa']))
    print('{}Desejamos um bom dia a todos !{}'.format(cores['ciano'], cores['limpa']))