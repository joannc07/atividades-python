def calculadora():
    operacao = input("Escolha uma operação (+, -, *, /): ")
    x = float(input("Digite o primeiro número: "))
    y = float(input("Digite o segundo número: "))

    if operacao == "+":
        soma = x + y
        print("O resultado da conta é: ", soma)

    elif operacao == "-":
        subtracao = x - y
        print("O resultado da conta é: ",subtracao)

    elif operacao == "*":
        multiplicacao = x * y
        print("O resultado da conta é: ",multiplicacao)

    elif operacao == "/":
        divisao = x / y
        print("O resultado da conta é: ", divisao)

    else:
        print("A operação não é válida")

calculadora()