factorial_cache = {}

def factorial(n):
    if n in factorial_cache:
        return factorial_cache[n]
    if n == 0 or n == 1:
        factorial_cache[n] = 1
    else:
        factorial_cache[n] = n * factorial(n - 1)
    return factorial_cache[n]

# Example usage:
number = 5
print(f"The factorial of {number} is {factorial(number)}")
print("Factorials stored in cache:", factorial_cache)
