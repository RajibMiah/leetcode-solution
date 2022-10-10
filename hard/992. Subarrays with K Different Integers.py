"""
Time O(N) for two passes.
Space O(K) at most K elements in the counter

using two-pointer technique and sliding window technique.
"""


def subarraysWithKDistinct(nums, k):
    def subarray(nums, k):
        visitedMap = dict()
        i, j = 0, 0
        result = 0

        while i < len(nums):

            if nums[i] in visitedMap:
                visitedMap[nums[i]] += 1
            else:
                visitedMap[nums[i]] = 1

            while(len(visitedMap) > k):

                visitedMap[nums[j]] -= 1
                if visitedMap[nums[j]] == 0:
                    del visitedMap[nums[j]]

                j += 1

            result += (i - j) + 1

            i += 1
        return result

    return subarray(nums, k) - subarray(nums, k - 1)


print(subarraysWithKDistinct([1, 2, 1, 2, 3], 2))  # output 7
