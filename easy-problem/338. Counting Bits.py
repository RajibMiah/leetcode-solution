
# Bruth force approacch
def _countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    total = 0
    arr = [0]
    for num in range(1, n+1):
        total = 0
        while(num):
            total += num % 2
            num //= 2
        arr.append(total)
    return arr


print(countBits(2))
print(countBits(5))
