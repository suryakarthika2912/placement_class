n = int(input("Enter a number:"))
found = False
while n > 0:
    digit = n % 10
    if (digit == 0): 
        found = True
        break
    n = n // 10
if (found):
    print("Yes, the number contains 0.")
else:
    print("No, the number does not contain 0.")