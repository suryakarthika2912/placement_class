arr = [5, 10, 15, 20, 25]
temp = arr[0]
arr[0] = arr[-1]
arr[-1] = temp
print("Array after swapping first and last elements:", arr)