class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0
        if m < len(nums1):
            while m < len(nums1):
                nums1.pop()
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                i = i + 1
            else:
                    nums1.insert(i , nums2[j])
                    m = m + 1
                    j = j + 1
        if i == m:
            while j < n:
                nums1.insert(m,nums2[j])
                m = m  + 1
                j = j +1
        print nums1

sol = Solution()
nums1 = [0]
nums2 = [1]
sol.merge(nums1,0,nums2,1)
