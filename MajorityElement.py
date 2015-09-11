class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[len(nums)/2]

sol = Solution()
nums = [2,4,5,5,5]
print sol.majorityElement(nums)
