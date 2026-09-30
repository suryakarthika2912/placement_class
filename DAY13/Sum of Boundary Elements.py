a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sum = 0

for i in range(3):
    for j in range(3):
        if i == 0 or i == 2 or j == 0 or j == 2:
            sum += a[i][j]

print("Sum of boundary elements =", sum)