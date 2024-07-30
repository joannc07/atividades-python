texto = input("Coloque uma palavra pare verificar se é considerada palíndroma : ")

# De acordo com que eu pesquisei, a expressão "::" significa um slicing, ou seja, é possível tirar uma substring de uma string. Logo, a expressão "[::-1]" irá inverter string.
if texto == texto[::-1]:
    
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")