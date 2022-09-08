import heapq


# time complexity is O(n log n) beacuse of  max heap implementation . other wishe you will do it by O(n^2) time complexity
def lastStoneWeight(stones):
    stones = [-i for i in stones]
    heapq.heapify(stones)
    while(len(stones) > 1):
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        if second > first:
            heapq.heappush(stones, first - second)
    stones.append(0)
    return abs(stones[0])


print(lastStoneWeight([2, 7, 4, 1, 8, 1]))
print(lastStoneWeight([1]))
