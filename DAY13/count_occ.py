a = [[1, 2, 3], [4, 5, 2], [7, 8, 9]]
key = 2
count = 0
for i in range(3):
    for j in range(3):
        if a[i][j] == key:
            count +=  1
print("Occurence=", count)            