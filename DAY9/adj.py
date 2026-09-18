n = [2, 5, 3, 7, 8, 4]
count = 0
for i in range(len(n) - 1):
    if n[i] < n[i + 1]:
        count += 1
print("Number of adjacent pairs:", count)        