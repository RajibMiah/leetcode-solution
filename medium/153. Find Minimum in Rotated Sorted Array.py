
"""

using binary search algorithm
rotate array

"""


def findMin(nums):
    l, r = 0, len(nums) - 1
    result = nums[0]

    while(l <= r):

        if nums[l] < nums[r]:
            result = min(result, nums[l])

        mid = l + (r - l) // 2
        result = min(result, nums[mid])
        if nums[mid] >= nums[l]:
            l = mid + 1
        else:
            r = mid - 1
    return result


print(findMin([3, 4, 5, 1, 2]))  # output 1
