def searchMatrix(matrix, target):

    if not matrix or target is None:
        return False
    cols, row = len(matrix[0]), len(matrix)
    i, j = 0, cols - 1

    while(i < row and j >= 0):

        if matrix[i][j] == target:
            return True

        if matrix[i][j] > target:
            j -= 1
        else:
            i += 1
    return False


print(searchMatrix([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [
      10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5))  # output True
