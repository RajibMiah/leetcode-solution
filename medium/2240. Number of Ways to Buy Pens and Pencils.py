def waysToBuyPensPencils(total, cost1, cost2):
    ans = 0

    for i in range((total//cost1) + 1):
        remining = total - (i * cost1)
        ans += ((remining // cost2)) + 1
    return ans


print(waysToBuyPensPencils(20, 10, 5))  # output 9
