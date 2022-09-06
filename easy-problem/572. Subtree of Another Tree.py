def isSubtree(root, subRoot):
    if root == None:
        return False
    elif isSameTree(root, subRoot):
        return True
    else:
        return isSubtree(root.left, subRoot) or isSubtree(root.right,  subRoot)


def isSameTree(root, subRoot):
    if root == None or subRoot == None:
        return root == None and subRoot == None
    elif root.val == subRoot.val:
        return isSameTree(root.left, subRoot.left) or isSameTree(root.right, subRoot.right)
    else:
        return False


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# root
a = TreeNode(3)  # [3,4,5,1,2]
b = TreeNode(4)
c = TreeNode(5)
d = TreeNode(1)
e = TreeNode(2)
# subRoot
f = TreeNode(4)
g = TreeNode(1)
h = TreeNode(2)

a.left = b
a.right = c
b.left = d
b.right = e

print(isSubtree())
