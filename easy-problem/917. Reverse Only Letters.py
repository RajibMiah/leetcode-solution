
"""
optimized in O(n) time compleixity and space complexity is O(n)
"""


def reverseOnlyLetters(s):

    string_list = list(s)
    i = 0
    j = len(s) - 1
    while(i < j):
        while(not s[i].isalpha() and i < j):
            i += 1
        while(not s[j].isalpha() and i < j):
            j -= 1

        string_list[i], string_list[j] = s[j], s[i]
        i += 1
        j -= 1

    return ''.join(string_list)


print(reverseOnlyLetters("a-bC-dEf-ghIj"))  # Output: "j-Ih-gfE-dCba"
