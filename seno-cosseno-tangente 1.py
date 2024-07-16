import math

angulo = float(input("Digite o valor do seu ângulo: "))

converter_rad = angulo * 3.141592 / 180
seno = math.sin(converter_rad)
cosseno = math.cos(converter_rad)
tangente = math.tan(converter_rad)

print("O seno de {}° é: {:.4}". format(angulo, seno))
print("O cosseno de {}° é: {:.4}". format(angulo, cosseno))
print("A tangente de {}° é: {:.4}". format(angulo, tangente))