# -*- coding:utf-8 -*-

class MaxDivision:
    def findMaxDivision(self, A, n):
        # write code here
        minvalue = min(A)
        maxvalue = max(A)
        distance = (maxvalue - minvalue)/float(n - 1)
        stat = [[maxvalue + 1,minvalue - 1] for col in range(n - 1)]
        for c in A:
            temp = min(int((c - minvalue)/distance),n-2)
            if stat[temp][0]  > c:
                stat[temp][0] = c
            if stat[temp][1] < c:
                stat[temp][1] = c
        ret = -1
        lastmin = stat[0][0]
        for i in range(n - 1):
            if stat[i][1] - stat[i][0] < 0:
                continue
            else:
                if ret < stat[i][1] - stat[i][0]:
                    ret = stat[i][1] - stat[i][0]
                if ret < stat[i][0] - lastmin:
                    ret = stat[i][0] - lastmin
                lastmin = stat[i][1]
        return ret


if __name__ == "__main__":
    sol = MaxDivision()
    print sol.findMaxDivision([1,3,5,8],4)
