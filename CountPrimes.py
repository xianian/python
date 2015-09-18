class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        flag = [True] * max(n,2)
        curval = 2
        flag[0] = False
        flag[1] = False
        while curval * curval < n:
            if flag[curval]:
                tmpval = curval * curval
                while tmpval < n:
                    flag[tmpval] = False
                    tmpval = tmpval + curval
            curval = curval + 1
        return sum(flag)

sol = Solution()
print sol.countPrimes(5)
