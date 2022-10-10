"""
NOTE: This problem is solved by  O(N) time complexity
"""


def findKthLargest(nums, k):

    k = len(nums) - k

    def quickselection(l, r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if p > k:
            return quickselection(l,  p - 1)
        if p < k:
            return quickselection(p + 1, r)
        else:
            return nums[p]
    return quickselection(0, len(nums) - 1)


print(findKthLargest([3, 2, 1, 5, 6, 4], 2))  # Output: 5
