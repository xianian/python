class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        alpha = {}
        for i in range(65,91):
            alpha[chr(i)] = i -64
        s = s[::-1]
        res = 0
        for i in range(len(s)):
            res = res + alpha[s[i]]* pow(26,i)
        return res

sol = Solution()
print sol.titleToNumber("Z")
