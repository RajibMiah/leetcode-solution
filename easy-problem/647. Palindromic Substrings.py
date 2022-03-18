
def CountPS(str ,n ):
    dp = [[0 for i in range(n)]
            for y in range(n)]
    count = 0

    for i in range(n):
        dp[i][i] = 1
        count += 1


    for i in range(n - 1):
        if(str[i] == str[i + 1]):
            dp[i][i + 1] = 1
            count += 1
   
    for gap in range(2 ,n ):
        for i in range(n - gap):
            j = gap + i
            if (str[i] ==  str[j] and dp[i + 1][ j - 1] == 1 ):
                dp[i][j]= 1
                count += 1
    return count

if __name__ == "__main__":
    str = "aaa"
    n = len(str)
    print(CountPS(str, n))