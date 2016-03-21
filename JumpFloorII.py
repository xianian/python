# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 2:
            return number
        else:
            a = list([1,2,4])
            for i in range(3,number,1):
                sum = 0
                for j in range(i):
                    sum += a[j]
                a.append(sum + 1)
            return a[number -1]

if __name__ == '__main__':
    sol = Solution()
    print sol.jumpFloor(5)
