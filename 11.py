def copy_file_contents(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            with open(destination_file, 'w') as dest:
                for line in src:
                    dest.write(line)
        print(f"Contents copied from {source_file} to {destination_file} successfully.")
    except FileNotFoundError:
        print(f"The file {source_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    source_file = input("Enter the name of the source file: ")
    destination_file = input("Enter the name of the destination file: ")
    copy_file_contents(source_file, destination_file)

if __name__ == "__main__":
    main()
