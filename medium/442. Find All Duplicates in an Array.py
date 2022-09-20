"""
time complexity is O(N) and space is constant O(1)
"""


def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    result = []
    for i in range(len(nums)):

        index = abs(nums[i]) - 1
        if nums[index] < 0:
            result.append(index + 1)
        nums[index] = -nums[index]

    return result


print(findDuplicates([4, 3, 2, 7, 8, 2, 3, 1]))  # Output: [2,3]
