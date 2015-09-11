# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self,root):
        if root:
            tmp = root.left
            root.left = root.right
            root.right = tmp
            self.dfs(root.left)
            self.dfs(root.right)

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.dfs(root)
        return root

sol = Solution()
root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(7)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(9)
result = sol.invertTree(root)
print result.val
# print root.left.val
# print root.right.val
# print root.left.left.val
# print root.left.right.val
# print root.right.left.val
# print root.right.right.val
