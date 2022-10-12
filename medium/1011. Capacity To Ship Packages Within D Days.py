def shipWithinDays(weights, days):
    def canShip(opacity):
        day = 1
        remain = opacity
        for weight in weights:
            if weight > opacity:
                return False
            remain -= weight
            if remain < 0:
                day += 1
                remain = opacity - weight
        return day <= days

    low = max(weights)
    high = 0

    for weight in weights:
        high += weight

    def binarySearch(low, high):

        if low > high:
            return low

        mid = low + (high - low) // 2

        if(canShip(mid)):
            return binarySearch(low, mid - 1)
        else:
            return binarySearch(mid + 1, high)

    # while(low < high):

    #     mid = (low + high) // 2

    #     if canShip(mid):
    #         high = mid
    #     else:
    #         low = mid + 1
    return binarySearch(low, high)


print(shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))  # Output: 15
