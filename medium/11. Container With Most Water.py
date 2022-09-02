
# time complexity O(N) and time complexity O(1)
def maxArea(height):
    areaLength = len(height)
    i = 0
    j = areaLength - 1
    max_area = 0
    while(i < j):
        new_area = min(height[i], height[j]) * (j - i)
        max_area = max(max_area, new_area)
        if(height[i] < height[j]):
            i += 1
        else:
            j -= 1
    return max_area

# Bruth Force approach /checking every possibility .
# the time complexity of this algorithm is O(N^2) and space complexity O(1)


def _maxArea(height):
    areaLength = len(height)
    i = 0
    max_area = 0
    while(i < areaLength):
        j = i + 1
        while(j < areaLength):
            new_max_area = min(height[i], height[j]) * (j - i)
            max_area = max(max_area, new_max_area)
            j += 1
        i += 1
    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # max area 49
print(maxArea([1, 1]))
