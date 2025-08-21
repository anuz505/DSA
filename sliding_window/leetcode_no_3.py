class Solution:
    def longestsubstring(self,s:str) -> int:
        l = 0
        n = len(s)
        longest = 0
        sett =  set()
        for r in range(n):
            # invalid
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            # valid
            sett.add(s[r])
            w = (r - l) + 1
            longest = max(longest, w)
        return longest
    
if __name__ == "__main__":
    S = Solution()
    s = "abcabcabb"
    result = S.longestsubstring(s)
    print(result)
