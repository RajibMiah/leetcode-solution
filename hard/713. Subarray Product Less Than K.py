


def xyz(nums , k):
    
    i , j = 0 , 0
    product = 1
    prodcut_dic = []

    if k <= 1: return 0
    # for z in nums:
    #     if z < k:
    #         prodcut_dic.append([z])

    while( j < len(nums)):
        product *=  nums[j]
        prodcut_dic.append([nums[j]])
        if product > k:
            while product > k:
                product //=  nums[i]
                i += 1
        
            if product < k :      
                prodcut_dic.append(nums[i:j - i + 1])  

        j += 1        

    print(prodcut_dic)    
    return len(prodcut_dic)       


print(xyz([10,5,2,6] , 100))
print(xyz([1,2,3] , 0))
print(xyz([50 , 15 , 5 , 1], 50))