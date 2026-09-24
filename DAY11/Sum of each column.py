arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for j in range(len(arr[0])):
    total = 0

    for i in range(len(arr)):
        total += arr[i][j]

    print("Column", j + 1, "sum =", total)