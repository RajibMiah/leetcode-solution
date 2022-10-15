def searchMatrix(matrix, target):
    if not matrix or target is None:
        return False

    rows, cols = len(matrix), len(matrix[0])
    low, high = 0, (rows * cols) - 1

    while low <= high:
        mid = low + (high - low) // 2
        # ( mid/cols ) for row index  and (mid % cols) for cols index
        if matrix[mid / cols][mid % cols] == target:
            return True
        elif matrix[mid / cols][mid % cols] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False


print(searchMatrix[[1, 3, 5, 7], [10, 11, 16, 20],
      [23, 30, 34, 60]], 3)  # output true
