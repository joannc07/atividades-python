import random
def jogo_advinhacao ():
    numero = random.randint(1, 5)
    numero_usuario = int(input("Coloque um número para tentar acertar: "))
    if numero_usuario == numero:
        print("Parabéns! Você acertou.")

    else:
        print("Você errou...")

    print("O número gerado foi: {}".format(numero))
jogo_advinhacao()