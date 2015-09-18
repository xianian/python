class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        vlist1 = version1.split('.')
        vlist2 = version2.split('.')

        count = 0
        ret = 0
        while count < len(vlist1) and count < len(vlist2):
            if int(vlist1[count]) < int(vlist2[count]):
                ret = -1
                break
            elif int(vlist1[count]) > int(vlist2[count]):
                ret = 1
                break
            else:
                count = count +1
        if count < len(vlist1) and count < len(vlist2):
            return ret
        if count  < len(vlist1):
            for i in range(count,len(vlist1)):
                if int(vlist1[i]) != 0:
                    ret = 1
                    break
        if count < len(vlist2):
            for i in range(count,len(vlist2)):
                if int(vlist2[i]) != 0:
                    ret = -1
                    break
        return ret

sol = Solution()
print sol.compareVersion("11","11.2")
