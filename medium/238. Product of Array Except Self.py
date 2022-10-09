
"""
    Time complexity is O(n) and space complxity is O(1) which is constatn ..
    array prepocessing techinque.
    prefix
    and post fix
"""


def productExceptSelf(self, nums):

    result = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]

    return result


print(productExceptSelf([1, 2, 3, 4]))  # Output: [24,12,8,6]
