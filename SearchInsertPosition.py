class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        # if nums[left] > nums[right]:
        #     nums.reverse()
        res = -1
        while left  < right:
            mid = left + (right - left)/2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                res = mid
                break
        if res == -1:
            if target <= nums[left]:
                res = left
            elif target > nums[right]:
                res = right + 1
            else:
                res = left + 1
        return res



nums = [1]
sol = Solution()

print sol.searchInsert(nums,1)
