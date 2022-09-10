# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        def dfs(root, currentSum):

            if not root:
                return False
            currentSum += root.val
            if not root.left and not root.right:
                return currentSum == targetSum

            return dfs(root.left, currentSum) or dfs(root.right, currentSum)

        return dfs(root, 0)
