def addStrings(num1, num2):
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    i = len(num1) - 1
    j = len(num2) - 1
    result = 0
    carry = 0
    ans = []
    while(i > - 1 or j > -1):
        d1 = ord(num1[i]) - ord('0') if i > -1 else 0
        d2 = ord(num2[j]) - ord('0') if j > -1 else 0
        sum = d1 + d2 + carry
        carry = sum / 10
        ans.append(chr(sum % 10 + ord('0')))
        i -= 1
        j -= 1

    return ''.join(ans)[::-1]


print(addStrings("123", "11"))
