class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lp = len(prices)
        if lp == 0:
            return 0
        
        lowest = float('inf')
        max_profit = 0
        
        for i in range(lp):
            if prices[i] < lowest:
                lowest = prices[i]
            else:
                profit = prices[i] - lowest
                if profit > max_profit:
                    max_profit = profit
        
        return max_profit

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5