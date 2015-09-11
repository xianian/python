import operator
class Solution(object):
    def func(self,n,k):
        if k == 0 or k == n:
            return 1
        else:
            return  reduce(operator.mul, range(n - k + 1, n + 1)) /reduce(operator.mul, range(1, k +1))

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        curRows = 0
        while curRows < numRows:
            curres = []
            for i in range(curRows + 1):
                curres.append(self.func(curRows,i))
            res.append(curres)
            curRows = curRows + 1
        return res

sol = Solution()
print sol.generate(5)
