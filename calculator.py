def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


def calculator():
    print("Simple Calculator")
    print("Type 'exit' to quit\n")

    while True:
        num1 = input("Enter first number: ")

        if num1.lower() == "exit":
            print("Calculator closed.")
            break

        operator = input("Enter operator (+, -, *, /): ")
        num2 = input("Enter second number: ")

        if num2.lower() == "exit":
            print("Calculator closed.")
            break

        try:
            num1 = float(num1)
            num2 = float(num2)

            if operator == "+":
                result = add(num1, num2)
            elif operator == "-":
                result = subtract(num1, num2)
            elif operator == "*":
                result = multiply(num1, num2)
            elif operator == "/":
                result = divide(num1, num2)
            else:
                result = "Invalid operator!"

            print("Result:", result)
            print()

        except ValueError:
            print("Invalid input! Please enter numeric values.\n")


if __name__ == "__main__":
    calculator()
