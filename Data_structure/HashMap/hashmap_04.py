from collections import defaultdict
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        charCount = defaultdict(int)
        var_map = defaultdict(list)
        for char in magazine:
            charCount[char] += 1
            var_map[char].append(charCount.values())

        for s in ransomNote:
            if charCount[s] == 0:
                return False
            charCount[s] -=1
        
        return True

if __name__ == "__main__":
    note = "aab"
    magazine = "aas"
    s = Solution()
    result = s.canConstruct(note,magazine)
    print(result)