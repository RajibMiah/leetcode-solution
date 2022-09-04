
def powerSum(arr, power=1):
    i = 0
    sum = 0
    while(i < len(arr)):
        if isinstance(arr[i], list):
            power += 1
            return sum + powerSum(arr[i], power)
        else:
            sum += arr[i]
        i += 1
    return pow(sum, power)


print(powerSum([1, 2, 3], 1))
print(powerSum([1, [1, 2]], 1))  # 8
print(powerSum([1, 2, [3, 4], [[2]]], 1))
