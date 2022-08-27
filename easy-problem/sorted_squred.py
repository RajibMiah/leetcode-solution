
def sortedSqured(arr):
    arr = [i*i for i in arr]  # It toke n time and space complexity
    arr.sort()  # nlogn time and space complexity
    return arr


print(sortedSqured([0, 5, 6, 8]))
print(sortedSqured([-2, -1, 0, 2, 5, 9]))
print(sortedSqured([0, 5, 6, 8]))
print(sortedSqured([2, 3, 3]))
print([])
