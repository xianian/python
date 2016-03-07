class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxv = nums[0]
        for i in range(len(nums)):
            if i == 0 or sums < 0:
                sums = nums[i]
            else:
                sums = sums + nums[i]
            if sums > maxv:
                maxv = sums
        return maxv

sol = Solution()
print sol.maxSubArray([-2])
