bases = [1, 2, 3, 4, 5]
exp = [2, 2, 2, 2, 2]
print('As bases são: ', bases)
print('Os expoentes são: ', exp)
resultado = [pow(bases, exp) for  bases, exp in zip (bases, exp)]
print('As potências são: ', resultado)
