arr = [10, 20, 30, 40, 50]
pos1 = 1
pos2 = 3
temp = arr[pos1]
arr[pos1] = arr[pos2]
arr[pos2] = temp
print("Array after swapping =", arr)