# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self,root):
        if root:
            return max(self.dfs(root.left),self.dfs(root.right)) + 1
        else:
            return 0

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            leftlen = self.dfs(root.left)
            rightlen = self.dfs(root.right)
            if abs(leftlen - rightlen) <= 1:
                if self.isBalanced(root.left):
                    return self.isBalanced(root.right)
                else:
                    return False
            else:
                return  False
        else:
            return True

sol =Solution()
root = TreeNode(1)
# root.left = TreeNode(2)
# #root.right = TreeNode(null)
# root.left.left = TreeNode(3)
# root.left.left.left = TreeNode(4)
# root.left.left.left.left = TreeNode(5)
print sol.isBalanced(root)
