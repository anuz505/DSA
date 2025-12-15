from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, profit, max_profit = 0, 0, 0, 0
        n = len(prices)
        for r in range(0, n - 1):
            if prices[r] < prices[l]:
                l = r
            else:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
        return max_profit


if __name__ == "__main__":
    S = Solution()
    prices = [10, 1, 5, 6, 7, 1]
    result = S.maxProfit(prices)
    print(f"The max profit is {result}")
