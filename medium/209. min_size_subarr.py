
def minSize(target, nums):
    infinity_num = 1000000
    i , j = 0 , 0
    total_sum = 0
    min_length = infinity_num
    while(j < len(nums)):
        total_sum += nums[j]
        while total_sum >= target:
            total_sum -= nums[i]
            min_length = min(min_length , len(nums[i:j+1]))
            i += 1
        j += 1
    if min_length == infinity_num:
        return 0      
    return min_length  


print(minSize(7,  [2,3,1,2,4,3]))  # 2
print(minSize(4, [1, 4, 4]))  # 1
print(minSize(11, [1, 1, 1, 1, 1, 1, 1, 1]))  # 0
