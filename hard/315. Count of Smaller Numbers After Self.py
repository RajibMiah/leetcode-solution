import bisect


def countSmaller(nums):

    arr, ans = sorted(nums), []

    for num in nums:
        i = bisect.bisect_left(arr, num)  # left most element of num
        ans.append(i)
        del arr[i]
    return ans


print(countSmaller([5, 2, 6, 1]))  # [2,1,1,0]
