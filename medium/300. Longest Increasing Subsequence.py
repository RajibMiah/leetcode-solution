"""
Using binary search algorithm Time complxity of O(nlogn) and space O(N)
"""
import bisect


def lengthOfLIS(nums):
    result = [nums[0]]

    for i in range(1, len(nums)):
        if result[-1] < nums[i]:
            result.append(nums[i])
        else:
            index = bisect.bisect_left(result, nums[i])
            result[index] = nums[i]

    return len(result)


print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # output 4
"""
using dp
"""


def _lengthOfLIS(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dp = [[0 for i in range(len(nums))] for j in range(len(nums))]

    def dfs(prev, current, nums, dp):

        if current == len(nums):
            return 0

        if prev != -1 and dp[prev][current] != 0:
            return dp[prev][current]
        left = 0
        if (prev == -1 or nums[prev] < nums[current]):
            left = 1 + dfs(current, current + 1, nums, dp)

        right = dfs(prev, current + 1, nums, dp)
        if prev != -1:
            dp[prev][current] = max(left, right)

        return max(left, right)

    return dfs(-1, 0, nums, dp)
