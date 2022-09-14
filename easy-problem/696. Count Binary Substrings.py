
def countBinarySubstrings(s):
    """
    :type s: str
    :rtype: int
    """
    consecutive = 1
    group = []
    res = 0
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            consecutive += 1
        else:
            group.append(consecutive)
            consecutive = 1
    group.append(consecutive)
    for j in range(1, len(group)):
        res += min(group[j], group[j - 1])
    print(group)
    return res


print(countBinarySubstrings("00110011"))  # output 6
print(countBinarySubstrings("10101"))  # output 4
