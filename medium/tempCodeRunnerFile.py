def maxSubArray(nums):
    ans = -100100
    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            ans = max(ans, cur_sum)
    return ans