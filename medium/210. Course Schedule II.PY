def findOrder(numCourses, prerequisites):
    """
    :type numCourses: int
    :type prerequisites: List[List[int]]
    :rtype: List[int]
    """

    preReq = {i: [] for i in range(numCourses)}
    visitedSet = set()
    cycle = set()
    output = []
    for i, courseDepend in prerequisites:
        preReq[i].append(courseDepend)

    def dfs(node):
        if node in cycle:
            return False
        if node in visitedSet:
            return True

        cycle.add(node)
        for cor in preReq[node]:
            if dfs(cor) == False:
                return False
        visitedSet.add(node)
        cycle.remove(node)
        output.append(node)
        return True

    # node means  course
    for node in range(numCourses):
        if dfs(node) == False:
            return []

    return output


print(findOrder(2, [[1, 0]]))
