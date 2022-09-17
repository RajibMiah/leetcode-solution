"""
The time complexity of O(n * m) and space complexity minmun between m and n O(n + m)
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):
    def isSameTree(self, r, t):
        if r == None or t == None:
            return r == None and t == None
        elif r.val == t.val:
            return self.isSameTree(r.left, t.left) and self.isSameTree(r.right, t.right)
        else:
            return False

    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if root == None:
            return False
        if self.isSameTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
