

def CountPS(str, n):
    dp = [[0 for i in range(n)]
          for y in range(n)]
    count = 0

    for i in range(n):
        dp[i][i] = 1
        count += 1  

    for col in range(1, n):
        for row in range(0 ,col):
            if ((row == col - 1) and str[col] == str[row]):
                dp[row][col] = 1
                count += 1
            elif (str[col] == str[row] and dp[row + 1][col - 1] == 1):
                dp[row][col] = 1
                count += 1          
    return count


if __name__ == "__main__":
    str = "racar"
    n = len(str)
    print(CountPS(str, n))
