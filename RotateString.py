# -*- coding:utf-8 -*-

class StringRotation:
    def rotateString(self, A, n, p):
        # write code here
        return A[p+1:n] + A[0:p+1]

if __name__ == "__main__":
    sol = StringRotation()
    print sol.rotateString('ABCDEFGH',8,4)
