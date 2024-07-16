print('----------- valor numérico -------------')
n1=(input('Digite um valor numérico: '))
print(n1.isnumeric())
print('')


print('------------ valor texto --------------')
t1=(input('Digitie outro valor ,porém que seja texto: '))
print(t1.isalpha())
print()

print('------------- valor texto númerico -------------')
a1=(input('Digite outro valor, porém que seja texto numérico: '))
print(a1.isalnum())
print()