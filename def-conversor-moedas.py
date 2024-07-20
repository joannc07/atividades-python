def conv_moedas ():
    moeda = str(input("Insira a moeda que você quer converter - (Real, Dólar americano, Euro, Libra esterlina): "))
    valor_moeda = float(input("Digite o valor da moeda: "))

    if moeda == "Real":
        dolar = valor_moeda / 5.60
        euro = valor_moeda / 6.10
        libra = valor_moeda / 7.23
        print(" valor R$ {} \n Dólar americano: US$ {} \n Euro: € {} \n Libra: £ {} ".format(valor_moeda, round(dolar, 2), round(euro, 2), round(libra, 2)))

    elif moeda == "Dólar americano":
        real = valor_moeda * 5.60
        euro = valor_moeda / 1.09
        libra = valor_moeda / 1.29
        print(" valor US$ {} \n Real: R$ {} \n Euro: € {} \n Libra: £ {} ".format(valor_moeda, round(real, 2), round(euro, 2), round(libra, 2)))

    elif moeda == "Euro":
        real = valor_moeda * 6.10
        dolar = valor_moeda * 1.09
        libra = valor_moeda / 1.19
        print(" valor € {} \n Real: R$ {} \n Dólar americano: US$ {} \n Libra: £ {} ".format(valor_moeda, round(real, 2), round(dolar, 2), round(libra, 2)))

    elif moeda == "Libra esterlina":
        real = valor_moeda * 7.23
        dolar = valor_moeda * 1.29
        euro = valor_moeda * 1.19
        print(" valor £ {} \n Real: R$ {} \n Euro: € {} \n Dólar americano: US$ {} ".format(valor_moeda, round(real, 2), round(euro, 2), round(dolar, 2)))

    else:
        print('moeda não reconhecida.')

conv_moedas()



