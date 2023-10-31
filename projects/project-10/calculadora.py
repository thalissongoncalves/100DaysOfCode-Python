import logo

#Calculator

operations_name = {}

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations_name["+"] = add
operations_name["-"] = subtract
operations_name["*"] = multiply
operations_name["/"] = divide


def calculator():
    print(logo.logo)
    num1 = float(input("Qual o primeiro número?: "))

    for symbol in operations_name:
        print(symbol)

    should_continue = True

    while should_continue:
        operation_symbol = input("Digite um operador: ")
        num2 = float(input("Qual o próximo número?: "))
        answer = operations_name[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Digite 's' para continuar calculando com {answer}, ou digite 'n' para começar um novo calculo: ") == "s":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()
