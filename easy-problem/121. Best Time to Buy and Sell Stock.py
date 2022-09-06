def maxProfit(prices):
    if len(prices) < 1:
        return 0
    i = 0
    max_profit = 0
    min_stock_price = prices[0]
    profit = 0
    while(i < len(prices)):
        if min_stock_price < prices[i]:
            profit = prices[i] - min_stock_price
            max_profit = max(max_profit, profit)
        else:
            min_stock_price = prices[i]
        i += 1
    return max_profit


print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([3, 1, 4, 8, 7, 2, 5]))
