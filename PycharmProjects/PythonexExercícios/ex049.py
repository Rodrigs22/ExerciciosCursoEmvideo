#meu jeito

'''
escolha = str(input('Escolha uma opção.  #tirei as 3 aspas para deixar como comentario
[ z ] taboada até o 10
escolha: ')).strip().lower()
n = int(input('
Escolha o numero da taboada
(OBS: Use ponto ''.'' e não virgula '','')
Número: '))
var = 10 * n
for c in range(0, var+1, +n):
    print(c)
'''

#jeito do guanabara

num = int(input('Digite um numero para saber sua taboada: '))
max = int(input('Até aonde você quer a taboada: ')) #eu adicionei essa linha ao algoritimo do guanabara
for c in range(1, max+1):  #adcionei o max+1 para que a linha acima funcionasse
    print('{} X {} = {}'.format(num, c, num*c))
