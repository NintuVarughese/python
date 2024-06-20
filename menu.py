def check(main_string, sub_string):
    return sub_string in main_string

def count(string, char):
    return string.count(char)

def replace(string, old_sub, new_sub):
    return string.replace(old_sub, new_sub)

def convert(string):
    return string.upper()

def menu():
    print("Menu:")
    print("1. Check if the String is a Substring of Another String")
    print("2. Count Occurrences of Character")
    print("3. Replace a Substring with Another Substring")
    print("4. Convert to Capital Letters")
    print("5. Exit")

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            main_string = input("Enter the main string: ")
            sub_string = input("Enter the substring: ")
            if check(main_string, sub_string):
                print(f"'{sub_string}' is a substring of '{main_string}'.")
            else:
                print(f"'{sub_string}' is not a substring of '{main_string}'.")

        elif choice == '2':
            string = input("Enter the string: ")
            char = input("Enter the character to count: ")
            count = count(string, char)
            print(f"The character '{char}' occurs {count} times in '{string}'.")

        elif choice == '3':
            string = input("Enter the string: ")
            old_sub = input("Enter the substring to replace: ")
            new_sub = input("Enter the new substring: ")
            result = replace(string, old_sub, new_sub)
            print(f"Resulting string: {result}")

        elif choice == '4':
            string = input("Enter the string: ")
            result = convert(string)
            print(f"String in capital letters: {result}")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
