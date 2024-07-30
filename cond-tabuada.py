numero = int(input("Coloque um número para ver sua tabuada: "))

for num in range(1, 11):
    print ("{} x {} = {} ".format(numero, num, numero*num))
