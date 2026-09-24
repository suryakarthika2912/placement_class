arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(arr)):
    total = 0

    for j in range(len(arr[i])):
        total += arr[i][j]

    print("Row", i + 1, "sum =", total)