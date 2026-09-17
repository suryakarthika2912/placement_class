nums = [1, 3, 6, 7, 8, 9]
n = int(input("Enter a number:"))
for i in range(len(nums)):
    if nums[i] == n:
        print(f"First occurrence of {n} is at index {i}")
        break
