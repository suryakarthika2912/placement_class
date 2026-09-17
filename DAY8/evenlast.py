nums = [1, 2, 4, 6, 7, 8, 9]
last = None
for i in nums:
    if i % 2 == 0:
        last = i
print("Last even number:", last)