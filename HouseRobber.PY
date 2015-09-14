class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = []
        a.append(0)
        lennums = len(nums)
        for i in range(lennums):
            if i < 2:
                if i == 0:
                    a.append(nums[i])
                elif nums[i - 1] > nums[i]:
                    a.append(nums[i - 1])
                else:
                    a.append(nums[i])
            else:
                if a[i - 1] > a[i - 2]:
                    maxvalue = a[i - 1] + nums[i]
                else:
                    maxvalue = a[i - 2] + nums[i]
                if a[i] < maxvalue:
                    a.append(maxvalue)
                else:
                    a.append(a[i])
        return a[lennums]

sol = Solution()
nums = [2,1]
print sol.rob(nums)
