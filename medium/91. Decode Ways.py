

def numDecodings(s):
    dp = {len(s): 1}

    def dfs(i):
        if i >= len(s):
            return 1
        if i in dp:
            return dp[i]
        if s[i] == "0":
            return 0
        result = dfs(i+1)
        if i + 1 < len(s) and (s[i] == '1' or s[i] == '2' and s[i+1] in '0123456'):
            result += dfs(i+2)
            dp[i] = result
        return result
    return dfs(0)


print(numDecodings("12"))
print(numDecodings("226"))
print(numDecodings("06"))
print(numDecodings("1201234"))
