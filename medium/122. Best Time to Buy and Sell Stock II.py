def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    i = 1
    max_price = 0
    while(i < len(prices)):
        if(prices[i] > prices[i - 1]):
            max_price += prices[i] - prices[i - 1]
        i += 1
    return max_price


print(maxProfit([7, 1, 5, 3, 6, 4]))
