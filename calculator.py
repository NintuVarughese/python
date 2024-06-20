def add(x,y):
    return x+y
def substract(x,y):
    return x-y
def mult(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        return "error"
    else:
        return x/y
def calculator():
    print("calculator")
    while True:
        print("\nOperations:")
        print("1. ADD")
        print("2. substraction")
        print("3. multifly")
        print("4. divide")
        print("5. exit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", substract(num1, num2))
            elif choice == '3':
                print("Result:", mult(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
        
        elif choice == '5':
            print("Thank you for using Simple Calculator. Goodbye!")
            break
        
        else:
            print("Invalid input. Please enter a valid number.")


calculator()










        
