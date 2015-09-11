# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self,root,res,sum):
        if root:
            res = res + root.val
            print res
            if not root.left and not root.right:
                if res == sum:
                    return True
            else:
                    return (self.dfs(root.left,res,sum) or self.dfs(root.right, res, sum))
                    return t1 or t2
            return False
        else:
            return False

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        return self.dfs(root,0,sum)

sol =Solution()
root = TreeNode(1)
root.left = TreeNode(-2)
root.right = TreeNode(-3)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
# root.left.left.left = TreeNode(7)
# root.left.left.right = TreeNode(2)
root.right.left =TreeNode(-2)
root.left.left.left = TreeNode(-1)
#root.right.right.right = TreeNode(1)
print sol.hasPathSum(root,-1)

