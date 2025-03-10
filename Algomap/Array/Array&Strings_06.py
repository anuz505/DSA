class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        
        min_len = len(strs[0])
        for s in strs:
            if len(s) < min_len:
                min_len = len(s)
   

        i = 0
        while i < min_len:
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
            i += 1
        return strs[0][:i]
    
if __name__ == "__main__":
    S = Solution()
    print(S.longestCommonPrefix(["flower", "flow", "flight"]))  # Output: "fl"
    print(S.longestCommonPrefix(["dog", "racecar", "car"]))  # Output: ""