def missingNumber(nums):
  
    def binarySearch(nums):
        l , r = 0 , len(nums)-1
        res = len(nums)
        while(l <= r):
            mid = l + ( r - l) //2
            if nums[mid] > mid:
                res , r = mid , mid - 1
            else:
                l = mid + 1
                
        return res
    
    return binarySearch(sorted(nums))

print(missingNumber([3,0,1])) #output 2
