import random

aluno1 = input('Digite o nome do primeiro')
aluno2 = input('Digite o nome do segundo')
aluno3 = input('Digite o nome do terceiro')
aluno4 = input('Digite o nome do quarto')
lista = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(lista)
print(f'O ganhador do sorteio foi o: {sorteio}.')
