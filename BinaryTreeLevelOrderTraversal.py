import Queue
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self,root,depth,res):
        if root:
            if len(res) < depth + 1:
                res.append([])
            res[depth].append(root.val)
            self.dfs(root.left,depth + 1,res)
            self.dfs(root.right,depth + 1, res)


    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root,0,res)
        return res

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
#root.right = TreeNode(null)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.left.left = TreeNode(5)
#root.left.right = TreeNode(null)
##root.right.right = TreeNode(null)

print sol.levelOrder([])
