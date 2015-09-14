class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        curcount = 1
        while True:
            if n >= pow(5,curcount):
                res = res + n / pow(5,curcount)
            else:
                break
            curcount = curcount + 1
        return res

sol = Solution()
print sol.trailingZeroes(10)
