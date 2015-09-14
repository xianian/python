class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        ret = True
        if num == 0:
            return False
        while True:
            if num == 1:
                break
            elif num % 2 == 0:
                num = num/2
            elif num %3 == 0:
                num = num/3
            elif num %5 == 0:
                num = num/5
            else:
                ret = False
                break
        return ret

sol = Solution()
print sol.isUgly(31)
