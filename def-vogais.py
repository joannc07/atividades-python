def vogais ():
    vogal = "aeiouAEIOU"
    contagem = 0
    palavra = (input("Digite uma palavra:"))

    for caractere in palavra:
     if caractere in vogal:
       contagem += 1
            
    print("A palavra {} possui o número de {} vogais". format(palavra, contagem))


vogais()


