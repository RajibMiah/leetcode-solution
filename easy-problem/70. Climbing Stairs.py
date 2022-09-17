class Solution(object):
    def dfs(self, n, memo=[]):
        if n == 0:
            return 1
        if n in memo:
            print(memo)
            return memo[n]

        if n < 0:
            return 0
        step = 0
        step += self.dfs(n-1, memo) + self.dfs(n - 2, memo)
        memo[n] = step
        return memo[n]

    def climbStairs(self, n):
        memo = [0] * (n + 1)
        return self.dfs(n, memo)
