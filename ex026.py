phrase = str(input(' Digite uma frase: '))
tradeA = phrase.replace('A', 'a')
print(
    f'Nesta frase tem {tradeA.count("a")} A.\n O primeiro A aparece na posição {tradeA.find("a") + 1}. E o ultimo na posição {tradeA.rfind("a") + 1}.'
)
