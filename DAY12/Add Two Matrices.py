a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]
c = [[9, 10], [11, 12]]
for i in range(2):
    for j in range(2):
        c[i][j] = a[i][j] + b[i][j]
print("Sum of matrices")
for i in range(2):
    for j in range(2):
        print(c[i][j], end =" ")
    print()    
        