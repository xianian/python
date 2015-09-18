class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        while n:
            res = res + chr((n - 1)%26 + 65)
            if n % 26 == 0:
                n = n - 26
            else:
                n = n - n %26
            n = n / 26
        res = res[::-1]
        return res

sol = Solution()
print sol.convertToTitle(702)
