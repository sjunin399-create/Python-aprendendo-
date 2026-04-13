import math

cateto1 = float(input('Digite o primeiro cateto: '))
cateto2 = float(input('Digite o segundo cateto: '))
raiz = math.sqrt((cateto1**2) + (cateto2**2))
print(f'A valor da hipotenusa é {raiz:.2f}')
