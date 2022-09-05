

def dfs(s, dp, i, result):
    if i in dp:
        return dp[i]
    if s[i] == 0:
        return s[i]
    result = dfs(s, dp, i+1, result)
    if i + 1 < len(s) and (s[i] == "1" or s[i] == '2' or s[i + 1] in "123456"):
        result += dfs(s, dp, i+2, result)
    return result


def numDecodings(s):
    dp = {len(s): 1}
    result = 0
    value = dfs(s, dp, 0, result)
    return value


print(numDecodings([121]))
