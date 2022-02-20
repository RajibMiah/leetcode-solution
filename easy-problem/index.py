
def xyz(s):
    list_s = set()
    for i in s:
        if i not in list_s:
            list_s.add(i)
        else:
            list_s.clear()  
    print(list_s)          
    return len(list_s)

print(xyz("abcabcbb"))