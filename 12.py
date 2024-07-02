import os
def create_directory(directory_name):
    try:
        os.makedirs(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")

def directory_listing(directory_name):
    try:
        files = os.listdir(directory_name)
        print(f"Listing for directory '{directory_name}':")
        for file in files:
            print(file)
    except FileNotFoundError:
        print(f"Directory '{directory_name}' not found.")

def search_py_files(directory_name):
    try:
        files = os.listdir(directory_name)
        print(f".py files in directory '{directory_name}':")
        for file in files:
            if file.endswith(".py"):
                print(file)
    except FileNotFoundError:
        print(f"Directory '{directory_name}' not found.")

def remove_file(file_path):
    try:
        os.remove(file_path)
        print(f"File '{file_path}' removed successfully.")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except PermissionError:
        print(f"Permission denied to remove file '{file_path}'.")

def main():
    while True:
        print("\nOptions:")
        print("1. Create a directory")
        print("2. Directory listing")
        print("3. Search for .py files")
        print("4. Remove a particular file")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            directory_name = input("Enter the name of the directory to create: ")
            create_directory(directory_name)
        elif choice == '2':
            directory_name = input("Enter the name of the directory to list: ")
            directory_listing(directory_name)
        elif choice == '3':
            directory_name = input("Enter the name of the directory to search for .py files: ")
            search_py_files(directory_name)
        elif choice == '4':
            file_path = input("Enter the path of the file to remove: ")
            remove_file(file_path)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
