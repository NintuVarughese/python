def pyramid(rows):
    for i in range(1,rows+1):
        for j in range(rows - i):
            print(" ",end=" ")
        for j in range(1, i + 1):
            print(j, end=" ")
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        print()
rows = int(input("Enter the number of rows for the pyramid: "))
pyramid(rows)

