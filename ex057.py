# minha versão
print("--" * 20)
print("ESSE PROGRAMA SÓ ACEITA M OU F !!")
print("--" * 20)
sexo = str(input("Digite seu sexo [M] ou [F] :")).lower()                     #input inicial para poder entrar no while
while sexo != "f" and sexo != "m":                                            #loop até que a pessoa digite f ou m
    print("Os unicos valores aceitos são [F] e [M].")
    sexo = str(input("Digite seu sexo novamente, [M] ou [F] :")).lower()      #input para receber e armazenar a resposta (.lower para formatar as letras para minuscula)
print("Agora sim, obrigado pela informação")
