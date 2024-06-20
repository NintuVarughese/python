def findnum():
    count = 0  
    sum = 0  

    for num in range(101, 200):
        if num % 7 == 0:
            count += 1 
            sum += num 

    return count, sum

count, sum = findnum()

print(f"Number of integers divisible by 7: {count}")
print(f"Sum of integers divisible by 7: {sum}")
