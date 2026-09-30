def longest_increasing_subsequence (nums):
    counter = 1
    while len(nums) > 1:
        print(nums)
        start = nums[0]
        print(start)
        count = 1
        for i in range(len(nums) - 1):
            if nums[i + 1] > start:
                count += 1
                start = nums[i + 1]
        nums.pop(0)
        if count > counter:
            counter = count
    return counter
    
nums = [10, 9, 2, 5, 3, 11, 101, 108]
print(longest_increasing_subsequence(nums))