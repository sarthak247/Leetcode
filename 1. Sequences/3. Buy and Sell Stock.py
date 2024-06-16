class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # Left and Right pointers
        maxProfit = 0 # MaxProfit

        while(r < len(prices)):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            r += 1    
        return maxProfit
        

# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/