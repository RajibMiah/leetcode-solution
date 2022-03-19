
def longPali(s):
    n = len(s)
    r = 0
    max_string = ''
    dp = [ [ 0 for i in range(n)]
                for j in range(n)]
    
    for i in range(n):
        dp[i][i] = 1

    for col in range(0 , n):
        for row in range(0 ,col):
            if(row == col-1 and s[col] == s[row]):
                dp[row][col] = 1
                if(max(r , row)):
                  r = row
                  max_string = s[row :col + 1]  
               
            elif(s[col] == s[row] and dp[row + 1][col -1] == 1):
                dp[row][col] = 1
                if(max(r , row)):
                  r = row
                  max_string = s[row :col + 1]  
                
    return max_string


if  __name__ == '__main__':
    s = "cbbd"
    print(longPali(s))


