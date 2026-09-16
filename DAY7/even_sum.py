nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for i in range(len(nums)):
    if i % 2 == 0:
        sum = sum + nums[i]
print(sum)