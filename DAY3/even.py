n = int(input("Enter a number:"))
count = 0
while n > 0:
    digits = n % 10
    if n % 2 == 0:
        count = count + 1
    n = n // 10
print("Number of even digits:", count)