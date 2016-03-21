# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        if number <= 3:
            return number
        else:
            a = list([1,2,3])
            for i in range(3,number,1):
                a.append(a[i-1] + a[i-2])
            return a[number -1]

if __name__ == '__main__':
    sol = Solution()
    print sol.jumpFloor(18)
