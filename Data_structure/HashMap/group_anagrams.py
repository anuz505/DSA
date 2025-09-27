from collections import defaultdict


class Solution:
    def sortme(self, strslist):

        hashmap = defaultdict(list)
        for strs in strslist:
            sorted_list = tuple(sorted(strs))
            hashmap[sorted_list].append(strs)

        return list(hashmap.values())


if __name__ == "__main__":
    s = Solution()
    input = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(s.sortme(input))
