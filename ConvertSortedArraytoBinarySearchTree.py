# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def dfs(self,root,no,nums):
        root = TreeNode(nums[no])
        if no * 2  + 1 < len(nums):
            self.dfs(root.left,no * 2 + 1,nums)
        if no * 2 + 2 < len(nums):
           self.dfs(root.right,no * 2 + 2)


    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        lennums = len(nums)
        root = None
        if lennums:
            self.dfs(root,0,nums)
        return root[0]

sol = Solution()
result = sol.sortedArrayToBST([1,2])
print result.left
