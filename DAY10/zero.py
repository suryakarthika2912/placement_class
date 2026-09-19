arr = [1, 0, 2, 3, 0, 4, 0, 5]
answer = []
for x in arr:
    if x != 0:
        answer.append(x)
for x in arr:        
    if x == 0:
        answer.append(x)
print(answer)