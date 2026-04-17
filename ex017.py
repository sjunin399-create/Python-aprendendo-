import math

cateto1 = float(input('Digite o primeiro cateto: '))
cateto2 = float(input('Digite o segundo cateto: '))
raiz = math.hypot(cateto1, cateto2)
print(f'A valor da hipotenusa é {raiz:.2f}')
