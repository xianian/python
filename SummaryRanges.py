class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        if len(nums) == 0:
            return res
        start = nums[0]
        end = start - 1
        for v in nums:
            if end + 1 == v:
                end = v
            else:
                if start != end:
                    res.append(str(start) + "->" + str(end))
                else:
                    res.append(str(start))
                start = v
                end = v
        if start != end:
            res.append(str(start) + "->" + str(end))
        else:
            res.append(str(start))
        return res

sol = Solution()
nums = [0,1,2,3,4,5,6]
print sol.summaryRanges([1])

