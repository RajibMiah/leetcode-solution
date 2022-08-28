
def monotonicArray(num):
    isAscending = isDecending = True
    for i in range(0, len(num) - 1):
        if num[i] > num[i+1]:
            isDecending = False
        elif num[i] < num[i + 1]:
            isAscending = False
    return isDecending or isAscending


print(monotonicArray([1, 2, 3]))
print(monotonicArray([1, 2, 2, 3]))
print(monotonicArray([1, 3, 2]))
print(monotonicArray([6, 5, 4, 4]))
