
# Bruth Force approach /checking every possibility
def maxArea(height):
    areaLength = len(height)
    i = 0
    max_area = 0
    while(i < areaLength):
        j = i + 1
        while(j < areaLength):
            new_max_area = min(height[i], height[j]) * (j - i)
            if (new_max_area > max_area):
                max_area = new_max_area
            j += 1
        i += 1
    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # max area 49
print(maxArea([1 , 1]))
