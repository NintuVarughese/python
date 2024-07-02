def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)
try:
    n = int(input("Enter a non-negative integer: "))
    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        result = recursive_sum(n)
        print(f"The sum of numbers from 0 to {n} is: {result}")
except ValueError:
    print("Invalid input. Please enter an integer.")
