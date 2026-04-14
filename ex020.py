import random

aluno1 = input('Dgite o nome do primeiro: ')
aluno2 = input('Dgite o nome do segundo: ')
aluno3 = input('Dgite o nome do terceiro: ')
aluno4 = input('Dgite o n]ome do quarto: ')
lista = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista)
print(f'A ordem embaralhada foi {lista}')
