import math

def resolver_equacao_segundo_grau(a, b, c):
    discriminamente = b**2 - 4*a*c

    if discriminamente > 0:
        
        x1 = (-b + math.sqrt(discriminamente)) / (2 * a)
        x2 = (-b - math.sqrt(discriminamente)) / (2 * a)
        
        return "Duas soluções reais = x1 = {}, x2 = {}". format(x1, x2)
    elif discriminamente == 0:
        x = -b / (2 * a)
        return "Umas solução real: x = {}".format(x)
    else:
        return "Nenhuma solução real"

a = float(input("Digite o coeficiente a(diferente de 0): "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

if a == 0:
    print("O coeficiente 'a' deve ser diferente de 0 para uma equação de segundo grau.")
else:
    resultado = resolver_equacao_segundo_grau (a,b,c)
    print (resultado)    