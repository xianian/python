class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        curvalue = 0
        lennums =  len(nums)
        i = 0
        while i < lennums:
            if curvalue == 2:
                break
            if nums[i] != curvalue:
                flag = 0
                for j in range(i,lennums):
                    if nums[j] == curvalue:
                        nums[i],nums[j] = nums[j],nums[i]
                        flag = 1
                        break
                if flag == 0:
                    curvalue = curvalue + 1
                    continue
            i  = i + 1
        print nums

sol = Solution()
sol.sortColors([0,0,1,2,1,0,1])

