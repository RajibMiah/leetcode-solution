import math


def coinChange(coins, amount, dp=[]):
    dp = [math.inf + 1] * (amount + 1)
    dp[0] = 0
    coins.sort()
    for m in range(1, amount + 1):
        for c in coins:
            if m >= c:
                dp[m] = min(dp[m], dp[m - c] + 1)
            else:
                break
    print(dp)
    return dp[amount] if dp[amount] != math.inf else - 1


print(coinChange([1, 4,  5], 11))
# print(coinChange([1, 2 , 5], 11))
