class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num != 0 and num != 9:
            return 1 + (num - 1)%9
        else:
            return num
