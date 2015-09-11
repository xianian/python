import operator
class Solution(object):
    def func(self,n,k):
        if k == 0 or k == n:
            return 1
        else:
            return  reduce(operator.mul, range(n - k + 1, n + 1)) /reduce(operator.mul, range(1, k +1))

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        for i in range(rowIndex + 1):
            res.append(self.func(rowIndex,i))
        return res

sol = Solution()
print sol.getRow(3)
