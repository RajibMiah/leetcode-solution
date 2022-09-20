def findMaxLength(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    array_map = {0: -1}
    count = 0
    max_length = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count -= 1
        else:
            count += 1

        if count in array_map:
            max_length = max(max_length, i - array_map[count])
        else:
            array_map[count] = i

    return max_length


print(findMaxLength([0, 1, 0]))  # outpue 2
