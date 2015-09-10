class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 1
        second = 2
        ret = n
        count = 2
        while (count < n):
            count = count + 1
            if count == n:
                ret = first + second
            else:
                tmp = first + second
                first = second
                second = tmp
        return ret

sol = Solution()
print sol.climbStairs(10)
