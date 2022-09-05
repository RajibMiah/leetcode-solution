import math


# Bruth Force approch time complexity O(N^2)
def maxSubArray(nums):
    max_sum = -100100
    for i in range(len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            max_sum = max(max_sum, sum)
    return max_sum

print(maxSubArray([1]))
print(maxSubArray([-2]))
print(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # out put  6 [4,-1,2,1]
print(maxSubArray([-5, 4, 6, -3, 4, -1]))
