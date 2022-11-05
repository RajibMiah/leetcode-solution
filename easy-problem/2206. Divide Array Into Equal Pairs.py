def divideArray(nums):
    memo = {}

    for i in nums:
        if i in memo:
            memo[i] += 1
        else:
            memo[i] = 1

    for i in memo:
        if memo[i] % 2 == 1:
            return False
    return True


print(divideArray([3, 2, 3, 2, 2, 2]))  # output True
