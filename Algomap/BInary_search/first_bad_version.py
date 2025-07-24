class Solution:
    def first_bad_version(self,n):
        l = 1
        r = n
        while l<r:
            m = (l + r) // 2
            if self.isBadVersion(m):
                r = m
            else:
                l = m + 1
        return l