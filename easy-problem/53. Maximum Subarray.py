class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum , curSum = nums[0] , nums[0]
        for i in range(1 ,len(nums)):
            curSum = max( curSum + nums[i] , nums[i]  )
            maxSum = max(maxSum  , curSum)
            
        return maxSum     