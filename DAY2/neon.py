n = int(input("Enter a number:"))
square = n * n
sum = 0
while square > 0: 
    digit = square % 10
    sum = sum + digit
    square = square // 10
if sum == n:
    print("It is neon number")
else:
    print("It is not neon number")