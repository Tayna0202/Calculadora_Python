print("CALCULADORA PYTHON")

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

operacao = int(input("Digite a operação desejada (Ex 1): "))

num1 = int(input("Digite o primeiro operador: "))

num2 = int(input("Digite o segundo operador: "))

match operacao:
        case 1:
            print("Operação de SOMA selecionada")
            resultado = num1 + num2
            print("A soma de " + str(num1) + " + " + str(num2) + " = " + str(resultado))
        case 2:
            print("Operação de SUBTRAÇÃO selecionada")
            resultado = num1 - num2
            print("A subtração de " + str(num1) + " - " + str(num2) + " = " + str(resultado))
        case 3:
            print("Operação de MULTIPLICAÇÃO selecionada")
            resultado = num1 * num2
            print("A multiplicação de " + str(num1) + " x " + str(num2) + " = " + str(resultado))
        case 4:
            print("Operação de DIVISÃO selecionada")
            resultado = num1 / num2
            print("A divisão de " + str(num1) + " / " + str(num2) + " = " + str(resultado))
