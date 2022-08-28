

def rotate(arr, step):
    if len(arr) < 0:
        return []
    k = step % len(arr)
    temp = arr[len(arr) - k: len(arr)]
    length = len(arr) - k - 1
    i = 0
    while(length >= 0):
        arr[length + k] = arr[length]
        length -= 1
    while(i < k):
        arr[i] = temp[i]
        i += 1
    return arr


print(rotate([1, 2, 3, 4, 5], 7))  # [4,5,1,2,3]
