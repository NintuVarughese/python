def print_pyramid(levels):
    for i in range(levels):
        
        for j in range(levels - i - 1):
            print(" ", end="")
        
        
        for k in range(2 * i + 1):
            print("*", end="")
        
        
        print()


levels = int(input("Enter the number of levels for the pyramid: "))
print_pyramid(levels)


