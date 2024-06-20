def recursive(n):
  if n == 0:
        return 0
  else:
        return n + recursive(n - 1)
result = recursive(10)
print("Sum of numbers from 0 to 10:", result)
