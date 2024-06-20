def reverse(num):
    original_num = num
    while True:
        num_str = str(num)
        reversed_num = int(num_str[::-1])
        new_sum = original_num + reversed_num
        if str(new_sum) == str(new_sum)[::-1]:
            print(f"Palindrome found: {new_sum}")
            break
        print(f"Sum is not a palindrome. Repeating with {new_sum}")
        num = new_sum
num = int(input("Enter a number: "))
reverse(num)
