class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = Counter(nums)
        for i in nums:
            if counter[i] == 1:
                return i      