class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for v in nums:
            if v not in res:
                res.append(v)
            else:
                res.remove(v)
        return res

sol = Solution()
print sol.singleNumber([1,2,1,3,2,5])
