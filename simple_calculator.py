"""Description: Ask user for two numbers and an operation (+, -, *, /).
 Use conditions to perform the correct calculation.
 Concepts Used: input(), float(), if-elif-else"""

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operation (+, -, *, /): ")

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero!")
else:
    print("Invalid operator.")
