def reverse_number(n):
    return int(str(n)[::-1])
def is_palindrome(n):
    return str(n) == str(n)[::-1]
def reverse_and_add(n):
    steps = 0
    while not is_palindrome(n):
        reversed_n = reverse_number(n)
        n += reversed_n
        steps += 1
        print(f"Step {steps}: {n}")
    return n, steps
def main():
    try:
        n = int(input("Enter a number: "))
        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            palindrome, steps = reverse_and_add(n)
            print(f"The palindrome is: {palindrome}")
            print(f"Number of steps: {steps}")
    except ValueError:
        print("Invalid input. Please enter an integer.")
if __name__ == "__main__":
    main()

