from collections import defaultdict


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)
        l, r = 0, 0
        k = len(s1)
        for i in range(len(s1)):
            s1_dict[s1[i]] += 1
        for r in range(len(s2)):
            s2_dict[s2[r]] += 1

            if r - l + 1 > k:
                s2_dict[s2[l]] -= 1
                if s2_dict[s2[l]] == 0:
                    del s2_dict[s2[l]]
                l += 1
            if r - l + 1 == k:
                if s1_dict == s2_dict:
                    return True

        return False
