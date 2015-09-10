# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p == None and q:
            return False
        elif q == None and p:
            return False
        elif p.val == q.val:
            if self.isSameTree(p.left, q.left):
                return self.isSameTree(p.right,q.right)
            else:
                return False
        else:
            return False

sol = Solution()
p = TreeNode(1)
q = None
print sol.isSameTree(p,q)
