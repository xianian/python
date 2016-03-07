class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sums = n*(n + 1)/2
        for v in nums:
            sums = sums - v
        return sums

sol = Solution()
print sol.missingNumber([0,1,3])
