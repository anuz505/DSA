from collections import defaultdict


class Solution:
    def majoritElement(self, nums):
        hashmap = defaultdict(int)
        for num in nums:
            hashmap[num] += 1
        for key, val in hashmap.items():
            if val > len(nums) // 2:
                return key


if __name__ == "__main__":
    S = Solution()
    input = [3, 2, 3]
    print(S.majoritElement(input))
