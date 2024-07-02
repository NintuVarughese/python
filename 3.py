def print_number_pyramid(rows):
    for i in range(1, rows + 1):
        for j in range(rows - i):
            print(" ", end="")
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
number_of_rows = 10
print_number_pyramid(number_of_rows)
