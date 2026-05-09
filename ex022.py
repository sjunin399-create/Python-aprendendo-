name = str(input('Qual seu nome completo: '))
pass1 = name.replace(' ', '')
print(
    f' Seu nome com todas letras maiusculas é: {name.upper()}\n Seu nome com todas letras minusculas: {name.lower()}\n Seu nome tem:{len(pass1)} letras.\n No seu primeiro nome tem {len(name.split()[0])} letras.'
)
