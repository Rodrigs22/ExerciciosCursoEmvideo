nome = str(input('digite seu nome: ')).strip()
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura (ex: 1.78): '))
peso = float(input('Digite seu peso em Kg: '))
imc = peso / (altura ** 2) # ** = altura ao quadrado
if imc < 18.5:
    print('Nome: {}'.format(nome))
    print('idade: {}'.format(idade))
    print('IMC: {:.1f}'.format(imc))
    print('Classificação: Abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('nome: {}'.format(nome))
    print('idade: {}'.format(idade))
    print('IMC: {:.1f}'.format(imc))
    print('classificação: Peso ideal')
elif imc >= 25 and imc < 30:
    print('nome: {}'.format(nome))
    print('idade: {}'.format(idade))
    print('IMC: {:.1f}'.format(imc))
    print('Classificação: Sobrepeso')
elif imc >= 30 and imc < 40:
    print('nome: {}'.format(nome))
    print('idade: {}'.format(idade))
    print('IMC: {:.1f}'.format(imc))
    print('Classificação: Obesidade')
elif imc >= 40:
    print('nome: {}'.format(nome))
    print('idade: {}'.format(idade))
    print('IMC: {:.1f}'.format(imc))
    print('Classificação: Obesidade Mórbida')
