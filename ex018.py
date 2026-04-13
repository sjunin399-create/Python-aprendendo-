import math
angulo = int(input('Qual o ângulo? '))
radianos = math.radiano(angulo)
seno = math.sin(radianos)
cosseno = math.coss(radianos)
tangente = math.tan(radianos)
print(f'O seno, cosseno e tangente do ângulo {angulo} e. \nSeno:{seno}.\nCosseno:{cosseno}.\nTangente:{tangente}.')