def canFinish(self, numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: bool
    """

    mapPre = {i: [] for i in range(numCourses)}
    visitSet = set()

    for i, pre in prerequisites:
        mapPre[i].append(pre)

    def dfs(node):

        if node in visitSet:
            return False
        if mapPre[node] == []:
            return True
        visitSet.add(node)
        for pre in mapPre[node]:
            if not dfs(pre):
                return False
        visitSet.remove(node)
        mapPre[node] = []
        return True

    for node in range(numCourses):
        print(node)
        if not dfs(node):
            return False

    return True
