import math

co = int(input('Digite o valor do cateto oposto: '))
ca = int(input('Digite o valor do cateto adjascente: '))
hip =  (co**2) + (ca**2)
print('O valor da hipotenusa é {}'. format(math.sqrt(hip)))