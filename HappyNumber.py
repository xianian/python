class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        numbers = []
        numbers.append(n)
        ret = True
        while True:
            strn = str(n)
            result = 0
            for v in strn:
                result = result + pow(int(v),2)
            if result == 1:
                break
            elif result not in numbers:
                numbers.append(result)
                n = result
            else:
                ret = False
                break
        return ret

sol = Solution()
print sol.isHappy(11)

