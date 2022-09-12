
def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]  
    """

    res = []
    nums.sort()
    for i, num in enumerate(nums):

        if i > 0 and num == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1

        while(l < r):
            threeSum = num + nums[l] + nums[r]
            if threeSum < 0:
                l += 1
            elif threeSum > 0:
                r -= 1
            else:
                res.append([num, nums[l], nums[r]])
                l += 1
                l += 1
                while(nums[l] == nums[l - 1] and l < r):
                    l += 1
    return res


print(threeSum([-1, 0, 1, 2, -1, -4]))  # Output: [[-1,-1,2],[-1,0,1]]
print(threeSum([0, 0, 0]))  # Output: [[0,0,0]]
