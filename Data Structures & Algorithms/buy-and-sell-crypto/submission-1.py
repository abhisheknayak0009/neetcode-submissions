class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        profit = 0
        for i in range(len(prices)):
            if(prices[i] < minPrice):
                minPrice = prices[i]
            else:
                profit = max(profit, prices[i]- minPrice)
        return profit