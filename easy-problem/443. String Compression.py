def compress(chars):
    i = 0
    j = 0
    index = 0
    while(i < len(chars)):
        while(j < len(chars) and chars[i] == chars[j]):
            j += 1
        chars[index] = chars[i]
        index += 1
        if(j - i > 1):
            l = str(j - i)
            for c in l:
                chars[index] = c
                index += 1
        i = j
    return index


# ["a","2","b","2","c","3"]
print(compress(["a", "a", "b", "b", "c", "c", "c"]))
print(compress(["a"]))  # return 1 ["a"]
print(compress(["a", "b", "b", "b", "b", "b",
      "b", "b", "b", "b", "b", "b", "b"]))  # return 4
