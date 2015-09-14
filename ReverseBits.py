class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0:
            return 0
        res = bin(n)[2:]
        res = "".join("0" for i in range(32-len(res))) + res
        res = res[::-1]
        return int(res,2)

sol = Solution()
print sol.reverseBits(0)
