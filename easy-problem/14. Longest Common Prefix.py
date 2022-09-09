def longestCommonPrefix(strs):
    if not strs:
        return ''
    min_string = min(strs, key=len)
    for i, ch in enumerate(min_string):
        for word in strs:
            if word[i] != ch:
                return min_string[:i]
    return min_string

print(longestCommonPrefix(["flower", "flow", "flight"]))  # "f1"
print(longestCommonPrefix(['fasf', 'faa', "fcsf"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
print(longestCommonPrefix(['aaa']))
print(longestCommonPrefix(['a']))
