a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
key = 5
found = False
for i in range(3):
    for j in range(3):
        if a[i][j] == key:
            found = True
if found:
    print("Element found")
else:
    print("Element not found")    
                
            
