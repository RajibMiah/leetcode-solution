import math


def coinChange(coins, amount, dp=[]):
    if amount in dp:
        return dp[amount]
    if amount == 0:
        return 0
    min_coins = float('inf')
    for c in coins:
        if amount >= c:
            total = coinChange(coins, amount - c, dp)
            min_coins = min(min_coins, total)
            dp[amount] = total
        return min_coins
    return min_coins


def _coinChange(coins, amount, dp=[]):
    dp = [math.inf + 1] * (amount + 1)
    dp[0] = 0
    # coins.sort()
    for m in range(1, amount + 1):
        for c in coins:
            if m >= c:
                dp[m] = min(dp[m], dp[m - c] + 1)
            else:
                break

    return dp[amount] if dp[amount] != math.inf else - 1


print(coinChange([1, 4,  5], 11))
# print(coinChange([1, 2 , 5], 11))
