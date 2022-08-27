
# with TIME COMPLEXITY O(n) AND SPACE COMPLEXITY O(n)
def sortedSqured(arr):
    startingIdx = 0
    endingIdx = len(arr) - 1
    result = [0 for i in range(len(arr))]
    for i in range(len(arr))[::-1]:
        startValue = arr[startingIdx] * arr[startingIdx]
        endingValue = arr[endingIdx] * arr[endingIdx]
        if startValue > endingValue:
            result[i] = startValue
            startingIdx += 1
        else:
            result[i] = endingValue
            endingIdx -= 1
    return result


# Broth Froce with time complextiy O(nlogn)
def sortedSqured(arr):
    arr = [i*i for i in arr]  # It toke n time and space complexity
    arr.sort()  # nlogn time and space complexity
    return arr


print(sortedSqured([0, 5, 6, 8]))
print(sortedSqured([-2, -1, 0, 2, 5, 9]))
print(sortedSqured([0, 5, 6, 8]))
print(sortedSqured([2, 3, 3]))
print([])
