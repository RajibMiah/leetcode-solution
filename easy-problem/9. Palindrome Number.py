# recursive way
def isPalindrome(x: int) -> bool:
        arr = str(x)
        n = len(arr)
        
        if n == 0:
            return True
        return palandrom(arr , 0 , n - 1)
    
    
def palandrom(x , l , r):
    
    if x[l] != x[r]:
        return False
    if(l <= r):
        palandrom(x , l+1 , r-1)
    return True   

#another way
def isPali(x):
    arr = str(x)
    reverseString = arr[::-1]
    if arr == reverseString:
        return True
    return False    


if  '__main__' == __name__:
#    print( isPalindrome(121))
     print(isPali(1000021))