class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        ret = True
        while n:
            if n == 1:
                break
            elif n %2 == 0:
                n = n /2
            else:
                ret = False
                break
        return ret

sol = Solution()
print sol.isPowerOfTwo(3)
