def reverse(arr, start, end):
    end -= 1
    while(start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end -= 1


# optimaized space complexity with removing oxilarry space


def rotate(arr, step):
    if len(arr) <= 0:
        return []
    k = step % len(arr)
    reverse(arr, 0, len(arr))
    reverse(arr, 0, k-1)
    reverse(arr, k, len(arr))
    return arr
# Brute Force solution


def _rotate(arr, step):
    if len(arr) <= 0:
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
