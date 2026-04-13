import math

angulo = int(input('Qual o ângulo? '))
radianos = math.radians(angulo)
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)
print(
    f'O seno, cosseno e tangente do ângulo {angulo} e. \nSeno:{seno}.\nCosseno:{cosseno}.\nTangente:{tangente}.'
)
