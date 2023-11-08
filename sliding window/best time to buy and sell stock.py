class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        lowest = 0 
        highest = 1
        maxprofit = 0 
        while highest < len(prices):
            print(lowest, highest)
            if prices[highest] - prices[lowest] > maxprofit:
                maxprofit = prices[highest] - prices[lowest]
            if prices[highest] < prices[lowest]:
                lowest = highest
            highest += 1
            
        return maxprofit