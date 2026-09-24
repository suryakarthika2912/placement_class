arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
smallest = arr[0][0]
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] < smallest:
            smallest = arr[i][j]
print("Smallest=", smallest)            
        