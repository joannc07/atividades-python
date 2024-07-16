
def conversor():
    temperatura = input("Escolha uma unidade de medida de temperatura (Celsius, Fahrenheit, Kelvin): ")
    valor_temp = int(input("Digite o valor da temperatura escolhida: "))

    if temperatura == "Celsius":
        Fahrenheit = (valor_temp * 9/5) + 32
        Kelvin = valor_temp + 273.15
        print("O resultado do Celsius em Fahrenheit é {} °F, e em Kelvin é {} K ".format(Fahrenheit, Kelvin))

    elif temperatura == "Fahrenheit":
        celsius = (valor_temp - 32) * 5/9
        kelvin =  (valor_temp - 32) * 5/9 + 273.15
        print("O resultado do Fahrenheit em Celsius é {} ºC, e em Kelvin é {} K ". format(celsius, kelvin))

    elif temperatura == "Kelvin":
        celsius = valor_temp - 273.15
        Fahrenheit = (valor_temp - 273.15) * 9/5 + 32
        print("O resultado do Kelvin em Celsius é {} ºC, e em Fahrenheit é {} ºF ".format(celsius, Fahrenheit))


conversor()