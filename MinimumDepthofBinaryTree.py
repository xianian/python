# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self,root,depth,minDepth):
        if root:
            if not root.left and not root.right:
                if minDepth[0] > depth + 1 or minDepth[0] == 0:
                    minDepth[0] = depth + 1
            if depth + 1 < minDepth[0] or minDepth[0] == 0:
                self.dfs(root.left,depth + 1,minDepth)
                self.dfs(root.right,depth + 1,minDepth)


    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        minDepth = [0]
        self.dfs(root,0,minDepth)
        return minDepth[0]

sol =Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)

print sol.minDepth(root)
