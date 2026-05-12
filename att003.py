number = input('Digite 11 numeros: ')
step1 = number[:3]
step2 = number[3:6]
step3 = number[6:9]
step4 = step1 + '.' + step2 + '.' + step3 + '-' + number[9:11:]
print(step4)