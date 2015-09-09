__author__ = 'Thinkpad'
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        lenlist = len(nums)
        naglist = []
        zerolist = []
        posilist = []
        retlist = []
        for i in range(lenlist):
            if nums[i] > 0:
                posilist.append(nums[i])
            elif nums[i] == 0:
                zerolist.append(nums[i])
            else:
                naglist.append(nums[i])
        zerolist.sort()
        posilist.sort()
        naglist.sort()
        lenzero = len(zerolist)
        lenposi = len(posilist)
        lennag = len(naglist)
        if(lenzero >= 3):
            retlist.append((0,0,0))
        if(lenzero > 0):
            for value in naglist:
                if value*(-1) in posilist:
                    curvalue = (value,0,-1 * value)
                    if curvalue not in retlist:
                        retlist.append(curvalue)
        if(lenposi >= 2 and lennag >= 1):
            for i in range(lenposi):
                for j in range(lenposi):
                    if i < j:
                        value = posilist[i] + posilist[j]
                        if value*(-1) in naglist:
                            curvalue = (-1 * value, posilist[i], posilist[j])
                            if curvalue not in retlist:
                                retlist.append(curvalue)
        if(lennag >= 2 and lenposi >= 1):
            for i in range(lennag):
                for j in range(lennag):
                    if i < j:
                        value = naglist[i] + naglist[j]
                        if value*(-1) in posilist:
                            curvalue = (naglist[i], naglist[j], -1 * value)
                            if curvalue not in retlist:
                                retlist.append(curvalue)

        return retlist

nums = []
sol = Solution()
print sol.threeSum(nums)