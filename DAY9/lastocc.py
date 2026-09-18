n = [5, 10, 15, 10, 20, 5, 10]
num = 5
last = -1
for i in range(len(n)):
    if n[i] == num:
        last = i
print("Last occurrence of", num, "is at index", last)
