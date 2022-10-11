
"""
 Solved with time complexity O( logn) and constant time complixity .
 This problem is sovled by binary search technique.

"""


def mySqrt(x):

    if x == 0:
        return 0
    start = 1
    end = x // 2
    ans = 1
    while(start <= end):
        mid = (start + end) // 2
        if mid * mid <= x:
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
    return ans


print(mySqrt(8))  # output 2
