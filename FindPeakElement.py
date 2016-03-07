class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lennums = len(nums)
        i = 0
        res = 0
        while i < lennums:
            if i == 0:
                if i + 1 < lennums and nums[i + 1] < nums[i]:
                    res = 0
                    break
                if i + 1 == lennums:
                    res = 0
                    break
            elif i == lennums - 1:
                if nums[i - 1] < nums[i]:
                    res = i
                    break
            else:
                if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]:
                    res = i
                    break
            i = i + 1
        return res

sol = Solution()
print sol.findPeakElement([1,2,3,4])

