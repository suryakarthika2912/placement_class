arr = [10, 5, 8, 3, 12, 6, 0, -4]

n = int(input("Enter number: "))

count = 0

for x in arr:
    if x > n:
        count += 1

print("Count =", count)