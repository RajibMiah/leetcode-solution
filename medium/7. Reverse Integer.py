def reverse(s):
    string_s = ''
    i = len(s)-1
    j = 0
    while(i >= 0):
        if s[i] not in '-+0':
            string_s += s[i]
            j += 1
        i -= 1

    return string_s


print(reverse("-1230"))
print(reverse("120))
