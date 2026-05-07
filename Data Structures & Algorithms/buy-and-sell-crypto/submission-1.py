class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = prices[0]
        for right in prices:
            currProfit = right-left
            profit = max(currProfit, profit)
            if right < left:
                left = right
        return profit