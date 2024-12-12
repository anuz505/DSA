class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sl = len(s)
        tl = len(t)
        i = 0
        j = 0
        while i < sl and j < tl:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == sl
    
if __name__ == '__main__':
    S = Solution()
    print(S.isSubsequence('abc','ahbgdc')) #True
    print(S.isSubsequence('axc','ahbgdc')) #False