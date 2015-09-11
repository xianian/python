import Queue
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSym(self,p,q):
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                if self.isSym(p.left,q.right):
                    return self.isSym(p.right,q.left)
                else:
                    return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None or root == []:
            return True
        else:
            return self.isSym(root.left,root.right)

sol = Solution()
root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.left.left = TreeNode(3)
# root.left.right = TreeNode(4)
# root.right.left = TreeNode(4)
#root.right.right = TreeNode(3)
print sol.isSymmetric([])
