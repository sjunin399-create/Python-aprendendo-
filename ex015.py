dias = float(input('Quantos dias o carro foi alugado? '))
km = int(input('Quantos km você dirigiu?'))
pagar = (dias * 60) + (km * 0.15)
print(f'O total a pagar é R${pagar}')