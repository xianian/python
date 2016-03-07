class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 and n == 1:
            return 1
        sums =   [[0 for col in range(n)] for row in range(m)]
        for i in range(m):
            sums[i][0] = 1
        for j in range(n):
            sums[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                sums[i][j] = sums[ i - 1][j] + sums[i][j - 1]
        return sums[m - 1][n - 1]

sol = Solution()
print sol.uniquePaths(3,7)
