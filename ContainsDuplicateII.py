class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        B = {}
        lennums = len(nums)
        res = False
        for i in range(lennums):
            if nums[i] not in B:
                B[nums[i]] = i
            else:
                if i - B[nums[i]] <= k:
                    res = True
                    break
                else:
                    B[nums[i]] = i
        return res

sol = Solution()
nums = [1,2,3,4,1]
print sol.containsNearbyDuplicate(nums,1)
