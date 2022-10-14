def searchInsert(nums, target):

    l, r = 0, len(nums) - 1

    def binarySearch(nums, l, r, target):

        while(l <= r):

            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return l

    return binarySearch(sorted(nums), l, r, target)


print(searchInsert([1, 3, 5, 6], 5))  # output  2
print(searchInsert([1, 3, 5, 6], 2))  # output 1
