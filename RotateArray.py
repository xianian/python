class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        while k:
            tmp = nums[-1]
            nums.pop()
            nums.insert(0,tmp)
            k = k - 1

sol = Solution()
nums = [1,2,3,4,5,6,7]
sol.rotate(nums,6)
print nums
