# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self,root,depth,maxdepth):
        if root:
            if maxdepth[0] < depth + 1:
                maxdepth[0] = depth + 1
            self.dfs(root.left,depth + 1,maxdepth)
            self.dfs(root.right,depth + 1, maxdepth)


    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        maxdepth = [0]
        depth = 0
        self.dfs(root, depth, maxdepth)
        return maxdepth[0]

sol =Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
print sol.maxDepth(root)
