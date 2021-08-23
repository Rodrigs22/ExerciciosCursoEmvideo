l1 = float(input('Digite o valor do primeiro lado: '))
l2 = float(input('Digite o valor do segundo lado: '))
l3 = float(input('Digite o valor do terceiro lado: '))
if l1 - l2 < l3 < l1 + l2:
    if l1 == l2 == l3:
        print('Essas medidas foram um tringualo EQUILÁTERO !')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Essas medidas foram um triangulo ISÓSCELES !')
    else:
        print('essas medidas forma  um triangulo ESCALENO !')
else:
    print('essas medidas NÃO formam um triangulo !')
