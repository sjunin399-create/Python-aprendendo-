name = str(input('Qual seu nome completo: '))
print(
    f' Seu nome com todas letras maiusculas é: {name.upper()}\n Seu nome com todas letras minusculas: {name.lower()}\n Seu nome tem: {len(name.replace(" ", ""))} letras.\n No seu primeiro nome tem {len(name.split()[0])} letras.'
)
