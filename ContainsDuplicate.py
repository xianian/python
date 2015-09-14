class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        B = {}
        ret = False
        for v in nums:
            if v not in B:
                B[v] = 1
            else:
                ret = True
                break
        return ret

sol = Solution()
nums = [1,2,3,4,1]
print sol.containsDuplicate(nums)
