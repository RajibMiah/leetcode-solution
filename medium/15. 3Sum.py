
# optimiazed solution . the time complexity of 3sum is O(N^2) AND space is O(n) (because of sorting)
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        ans = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while(l < r):
                currentSum = num + nums[l] + nums[r]
                if currentSum > 0:
                    r -= 1
                elif currentSum < 0:
                    l += 1
                else:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    while(nums[l] == nums[l - 1] and l < r):
                        l += 1
        return ans
