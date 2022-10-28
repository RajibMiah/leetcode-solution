"""
 Time Complexity O(n)

"""


def minPartitions(n):

    ans = 0

    for i in n:
        current = ord(i) - 48
        ans = max(ans, current)
    return ans


print(minPartitions("82734"))  # output 8
