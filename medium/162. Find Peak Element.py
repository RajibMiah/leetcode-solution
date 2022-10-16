"""
TIme complixty is O(log n)
space complixity is constatnt O(1)
"""


def findPeakElement(nums):

    l, r = 0, len(nums) - 1
    result = 1
    if len(nums) == 2 and nums[0] < nums[1]:
        return 1

    while(l <= r):

        mid = l + (r - l) // 2

        if nums[mid] >= nums[mid - 1]:
            result = mid
            l = mid + 1
        else:
            r = mid - 1
    return result


print(findPeakElement([1, 2, 3, 1]))  # Output: 2
