"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


def cloneGraph(self, node):
    """
    :type node: Node
    :rtype: Node
    """
    newGraph = {}

    def dfs(node):
        if node in newGraph:
            return newGraph[node]
        copy = Node(node.val)
        newGraph[node] = copy
        for nei in node.neighbors:
            copy.neighbors.append(dfs(nei))
        return copy

    return dfs(node) if node else []


print(cloneGraph([[2, 4], [1, 3], [2, 4], [1, 3]]))
