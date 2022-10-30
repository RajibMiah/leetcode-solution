
"""
time complixty is O(log 5 ^ n) and space complxity is constant

"""


def trailingZeroes(n):
    count = 0

    while n:
        n /= 5
        count += n

    return count


print(trailingZeroes(5))  # output 1
