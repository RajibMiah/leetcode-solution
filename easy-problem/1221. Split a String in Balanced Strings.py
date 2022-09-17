
"""
this problem is solve by greedy approach . the time complexity of this algorithom is O(N)
and the space complexity is O(1)
"""


def balancedStringSplit(s):
    """
    :type s: str
    :rtype: int
    """
    i = 0
    count = 0
    result = 0
    for i in range(len(s)):
        if s[i] == 'R':
            count += 1
        elif s[i] == 'L':
            count -= 1

        if count == 0:
            result += 1
    return result


print(balancedStringSplit("RLRRRLLRLL"))  # 2
