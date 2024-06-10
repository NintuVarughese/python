n1 = int(input("Enter the first number for calculation: "))
n2 = int(input("Enter the second number for calculation: "))
op = input("Enter the operation you want to perform (+, -, *, /): ")

if op == "+":
    result = n1 + n2
elif op == "-":
    result = n1 - n2
elif op == "*":
    result = n1 * n2
elif op == "/":
    if n2 == 0:
        print("Error: Division by zero")
    else:
        result = n1 / n2
        print("Result is:", result)
else:
    print("Invalid operation")

if op in ["+", "-", "*"]:
    print("Result is:", result)
