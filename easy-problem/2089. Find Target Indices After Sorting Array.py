def targetIndices(nums, target):
    low, high = 0, len(nums)
    for n in nums:
        if n > target:
            high -= 1
        elif n < target:
            low += 1
    return range(low, high)


print(targetIndices([1, 2, 5, 2, 3], 2))  # Output: [1,2]
