
def longPali(s):
    n = len(s)
    dp = [[0 for i in range(n)]
          for j in range(n)]
    max_length = 0
    start = 0
    for i in range(n):
        dp[i][i] = 1

    for col in range(1, n):
        for row in range(0, col):
            if(row == col-1 and s[row] == s[col]):
                dp[row][col] = 1
                if col > max_length:
                    start = row
                    max_length = 1

            elif(s[col] == s[row] and dp[row + 1][col - 1] == 1):
                dp[row][col] = 1
                if col > max_length:
                    start = row
                    max_length = col

    print(start, max_length)

    return s[start: max_length + 1]


if __name__ == '__main__':
    # s = "aaaaaaaaa"
    # print(longPali(s))
    # "aaaaabaaaaa"
    # "aaajaabbbaac"
    # "cbbd"
    # "ac"
    # "ccd"
    st = "ccd"
    l = longPali(st)
    print(l)
