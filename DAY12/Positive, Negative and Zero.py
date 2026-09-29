a = [
    [10, -5, 0],
    [-2, 8, 4],
    [0, -7, 6]
]

for i in range(3):
    for j in range(3):
        if a[i][j] > 0:
            print(a[i][j], "Positive")
        elif a[i][j] < 0:
            print(a[i][j], "Negative")
        else:
            print(a[i][j], "Zero")