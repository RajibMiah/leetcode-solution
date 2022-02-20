
def findLognSub(s):
    result = []
    str = list(s)
    i , j =  0 , 0
    n = len(str)
    max_length = 0
    while(j < n):
        if str[j] not in  result:
            result.append(str[j])
            if (j - i + 1 < n):
                j += 1
        else:
            max_length = max(max_length , len(result))
            result.pop(0)
            i += 1
        if( j == n):
             max_length = max(max_length , len(result))
             break
    return max_length
    
print(findLognSub("dvdf"))
print(findLognSub('bbbbb'))
print(findLognSub("abcabcbb"))
print(findLognSub('pwwkew'))