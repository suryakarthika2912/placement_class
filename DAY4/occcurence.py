n = int(input("Enter the numbers:"))
target = int(input("Enter the target:"))
count = 0
while n > 0:
    digit = n % 10
    if digit == target:
        count += 1
    n = n // 10
print("The target digit occurs", count, "times in the number.")
