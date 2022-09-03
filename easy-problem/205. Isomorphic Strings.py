from asyncio.windows_events import NULL


def isIsomorphic(s, t):
    shash = {}
    thash = {}
    if len(s) != len(t):
        return False
    for s1, t1 in zip(s, t):
        if not shash.get(s1):
            shash[s1] = t1
        if not thash.get(t1):
            thash[t1] = s1
        if shash[s1] != t1 or thash[t1] != s1:
            return False

    return True


print(isIsomorphic("egg", "add"))
print(isIsomorphic("foo", "bar"))
print(isIsomorphic("paper", "title"))
print(isIsomorphic("badc", "baba"))
print(isIsomorphic('ababr', 'eoeoo'))
