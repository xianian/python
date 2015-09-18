# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self,root,depth,path,res):
        if root:
            if len(path) < depth + 1:
                if depth != 0:
                    path.append("->" + str(root.val))
                else:
                    path.append(str(root.val))
            else:
                path[depth] = "->" + str(root.val)
            if root.left == None and root.right == None:
                tmp = path[0:depth + 1]
                res.append(''.join(tmp))
            else:
                self.dfs(root.left, depth+1,path,res)
                self.dfs(root.right,depth + 1,path,res)

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        self.dfs(root,0,[],res)
        return res

sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
print sol.binaryTreePaths(root)
