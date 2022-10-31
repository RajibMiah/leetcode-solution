def hasAlternatingBits(n):
    x = n % 2
    while(n):
        y = x
        n = n >> 1
        x = n % 2
        if x == y:
            return False
    return True


print(hasAlternatingBits(5))  # output True
