def isIsomorphic(s, t):
    maptable = {}
    sLength = len(s)
    i = 0
    while(i < sLength):
        if s[i] in maptable:
            if maptable[s[i]] != t[i]:
                return False
        maptable[s[i]] = t[i]
        i += 1

    return True


print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("paper", "title"))
print(isIsomorphic("badc", "baba"))
