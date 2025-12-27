number1 = float(input("Enter a number: "))
operation = input("Enter an operation (+, -, *, /): ")
number2 = float(input("Enter a number: "))

def add( num1, num2):
    return num1 + num2

def subtract( num1, num2):
    return num1- num2

def multiply( num1, num2):
    return num1 * num2

def divide( num1, num2):
    return num1 / num2

if operation == "+":
    print(add(number1, number2))

elif operation == "-":
    print(subtract(number1, number2))

elif operation == "*":
    print(multiply(number1, number2))

elif operation == "/":
    print(divide(number1, number2))