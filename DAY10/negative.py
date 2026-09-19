arr = [-1, 0, -2, -3, 0, -4, 0, -5]
result = []
for x in arr:
    if x < 0:
        result.append(x)
for x in arr:
    if x >= 0:
        result.append(x)
print(result)