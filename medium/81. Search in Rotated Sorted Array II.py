def search(nums, target):

    l, r = 0, len(nums) - 1

    while(l <= r):

        mid = l + (r - l) // 2

        if nums[mid] == target:
            return True
        if nums[mid] == nums[l] and nums[mid] == nums[r]:
            l += 1
            r -= 1
        elif nums[l] <= nums[mid]:
            if nums[mid] >= target and nums[l] <= target:
                r = mid-1
            else:
                l = mid+1

        else:
            if target >= nums[mid] and target <= nums[r]:
                l = mid+1
            else:
                r = mid-1

    return False


print(search([2, 5, 6, 0, 0, 1, 2], 0))  # output True
# Output True
print(search([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1], 2))
