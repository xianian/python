class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lennums = len(nums)
        count = 0
        i = 0
        while i + count < lennums:
            if nums[i] == 0:
                for j in range(i,lennums - 1 - count):
                        tmp = nums[j + 1]
                        nums[j + 1] = nums[j]
                        nums[j] = tmp
                count = count + 1
            if nums[i] != 0:
                i = i + 1
        return nums

sol = Solution()
print sol.moveZeroes([0,1,0,3,12])
