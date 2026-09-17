arr = [1, 2, 3, 4, 5]
total = 0
for x in arr:
    total = total + x
avg = total / len(arr)
count = 0
for x in arr:
    if x > avg:
        count += 1
print("Average:", avg)
print("Count of numbers greater than average:", count)