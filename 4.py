count = 0
total_sum = 0
for number in range(101, 200):
    if number % 12 == 0:
        count += 1
        total_sum += number
print("Number of integers divisible by 12:", count)
print("Sum of integers divisible by 12:", total_sum)
