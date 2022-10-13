

"""

this problem is solve by O( logn ) time complexity .where Binary search technique is used

"""


def searchRange(nums, target):

    def binarySearch(isLeft):
        left, right = 0, len(nums) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                result = mid
                if isLeft:
                    right = mid - 1  # find the first occurence, look to the left
                else:
                    left = mid + 1  # find the last occurence, look to the right

        return result

    return [binarySearch(True), binarySearch(False)]


print(searchRange([5, 7, 7, 8, 8, 10], 8))  # Output: [3,4]
