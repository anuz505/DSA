from collections import defaultdict


class Solution:
    # brute force
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        n = len(s)
        max_len = 0
        chars = defaultdict(int)
        for r in range(n):
            chars[s[r]] += 1
            count_most_frequent_char = max(chars.values())
            w_size = r - l + 1
            if w_size - count_most_frequent_char > k:
                chars[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len

    def characterReplacementOptim(self, s: str, k: int) -> int:
        chars = defaultdict(int)
        max_len = 0
        l = 0
        max_f = 0
        for r in range(len(s)):
            chars[s[r]] += 1
            max_f = max(max_f, chars[s[r]])

            if ((r - l + 1) - max_f) > k:   
                chars[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
        return max_len


if __name__ == "__main__":
    s = "AABABBA"
    k = 2
    sol = Solution()
    print(sol.characterReplacement(s, k))
