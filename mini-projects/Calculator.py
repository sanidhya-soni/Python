def add(a, b):
    """Takes two numbers and returns their sum !"""
    return a + b


def subtract(a, b):
    """Takes two numbers and returns their difference !"""
    return a - b


def multiply(a, b):
    """Takes two numbers and returns their product !"""
    return a * b


def divide(a, b):
    """Takes two numbers and returns their division !"""
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
for symbol in operations:
    print(symbol)
symbol = input("Enter the symbol of Operation you want to perform: ")
calculation_fun = operations[symbol]
print(num1, symbol, num2, "=", calculation_fun(num1, num2))
