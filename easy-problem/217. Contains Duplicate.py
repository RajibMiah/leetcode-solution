def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    memo = set()
    for i in nums:
        if i in memo:
            return True
        memo.add(i)

    return False


print(containsDuplicate([1, 2, 3, 1]))  # output True
print(containsDuplicate([1, 2, 3, 4]))  # output False
