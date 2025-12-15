# maximum sum
from typing import List


class Solution:
    def max_sum_sliding_window(self, arr: list) -> int:
        l, r, w_sum = 0, 0, 0
        k = 3
        max_sum = 0
        n = len(arr)
        for r in range(0, n):
            w_sum += arr[r]

            if r >= k - 1:
                max_sum = max(max_sum, w_sum)
                w_sum -= arr[l]
                l += 1
        return max_sum


if __name__ == "__main__":
    arr = [2, 1, 5, 1, 3, 2]
    S = Solution()
    result = S.max_sum_sliding_window(arr)
    print(f"max_sum:{result}")
