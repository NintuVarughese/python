def is_substring(s1, s2):
    return s1 in s2

def count_occurrences(s, char):
    return s.count(char)

def replace_substring(s, old_sub, new_sub):
    return s.replace(old_sub, new_sub)

def convert_to_capital(s):
    return s.upper()

def main():
    while True:
        print("\nMenu:")
        print("1. Check if the String is a Substring of Another String")
        print("2. Count Occurrences of Character")
        print("3. Replace a Substring with Another Substring")
        print("4. Convert to Capital Letters")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            s1 = input("Enter the first string: ")
            s2 = input("Enter the second string: ")
            if is_substring(s1, s2):
                print(f'"{s1}" is a substring of "{s2}"')
            else:
                print(f'"{s1}" is not a substring of "{s2}"')

        elif choice == '2':
            s = input("Enter the string: ")
            char = input("Enter the character to count: ")
            count = count_occurrences(s, char)
            print(f'The character "{char}" occurs {count} times in the string.')

        elif choice == '3':
            s = input("Enter the string: ")
            old_sub = input("Enter the substring to replace: ")
            new_sub = input("Enter the new substring: ")
            result = replace_substring(s, old_sub, new_sub)
            print(f'The new string is: "{result}"')

        elif choice == '4':
            s = input("Enter the string: ")
            result = convert_to_capital(s)
            print(f'The string in capital letters is: "{result}"')

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
