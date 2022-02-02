class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, low = 0, prices[0]
        for p in prices[1:]:
            if p < low: low = p
            else: profit = max(profit, p - low)
        return profit
        