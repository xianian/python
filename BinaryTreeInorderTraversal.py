# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self,root,res):
        if root:
            self.dfs(root.left,res)
            res.append(root.val)
            self.dfs(root.right,res)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        self.dfs(root,res)
        return res

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

print sol.inorderTraversal(root)


