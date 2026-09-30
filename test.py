nums = [10, 9, 2, 5, 3, 11, 101, 108]
high = []

while len(nums) > 1:
    start = nums[0]
    count = 1
    for i in range (len(nums) - 1):
        if nums[i+1] > start:
            count += 1
            start = nums[i+1]
    high.append(count)
    nums.pop(0)

print()
print(high)