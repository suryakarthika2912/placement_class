a = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

n = 3
sum = 0

for i in range(n):
    sum = sum + a[i][i]
    sum = sum + a[i][n - 1 - i]

print("Sum of both diagonals =", sum)